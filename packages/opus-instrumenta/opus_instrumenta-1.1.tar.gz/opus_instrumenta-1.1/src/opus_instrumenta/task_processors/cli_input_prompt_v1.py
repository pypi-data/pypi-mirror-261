import json
import traceback
from getpass import getpass
import copy
import signal
import contextlib

from magnum_opus.operarius import LoggerWrapper, TaskProcessor, KeyValueStore, Task, StatePersistence


class TimeoutException(Exception):
    pass


@contextlib.contextmanager
def timeout_context(seconds):
    def signal_handler(signum, frame):
        raise TimeoutException("Timed out!")
    signal.signal(signal.SIGALRM, signal_handler)
    signal.alarm(seconds)
    try:
        yield
    finally:
        signal.alarm(0)


def get_normal_user_input_with_timeout(prompt_char: str='> ', timeout_seconds: int=10, default_value: str=''):
    result = default_value
    try:
        with timeout_context(timeout_seconds):
            result = input(prompt_char)
            if result == '':
                result = default_value
    except TimeoutException:
        print(default_value)
    return result


def get_password_input_with_timeout(prompt_char: str='> ', timeout_seconds: int=10, default_value: str=''):
    result = default_value
    try:
        with timeout_context(timeout_seconds):
            result = getpass(prompt=prompt_char)
            if result == '':
                result = default_value
    except TimeoutException:
        print()
    return result


class CliInputPrompt(TaskProcessor):

    def __init__(self, kind: str='CliInputPrompt', kind_versions: list=['v1',], supported_commands: list = list(), logger: LoggerWrapper = LoggerWrapper()):
        self.spec = dict()
        self.metadata = dict()
        super().__init__(kind, kind_versions, supported_commands, logger)

    def process_task(self, task: Task, command: str, context: str = 'default', key_value_store: KeyValueStore = KeyValueStore(), state_persistence: StatePersistence = StatePersistence()) -> KeyValueStore:
        """This task will prompt a user for input. If no input is provided with an (optional) timeout, a default value 
        will be used. The user input value will be added to the `KeyValueStore`.
        
        Regardless of command and context, the specified shell script will be run, unless specifically excluded.

        # Spec fields

        Root levels spec fields

        | Field                         | Type    | Required | In Versions | Description                                                                                                                                                                                                          |
        |-------------------------------|:-------:|:--------:|:-----------:|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
        | `promptText`                  | String  | No       | v1          | The text to display on screen. If set, must be a string with minimum length of 2 and less then 80 characters.                                                                                                        |
        | `defaultValue`                | String  | No       | v1          | If defined, this will be the default value a user can choose by just pressing ENTER, or it will also be the value used after the `waitTimeout` expires.                                                              |
        | `promptCharacter`             | String  | No       | v1          | The character for the actual prompt. If set, must be a string with minimum length of 1 and less then 8 characters.                                                                                                   |
        | `waitTimeoutSeconds`          | Integer | No       | v1          | Default is "0" (do not expire - wait forever). Any value >0 but <3600 (1 hour) will wait for user input. When the timeout is reached, the default value will be used.                                                |
        | `convertEmptyInputToNone`     | Boolean | No       | v1          | If input is empty, convert the final value to NoneType                                                                                                                                                               |
        | `maskInput`                   | Boolean | No       | v1          | If true, do not echo characters. This is suitable to ask for a password, for example                                                                                                                                 |


        Args:
            task: The `Task` of kind `ShellScript` version `v1` to process
            command: The command is ignored for ShellScript processing - any task of this kind will ALWAYS be processed regardless of the command.
            context: The context is ignored for ShellScript processing - any task of this kind will ALWAYS be processed regardless of the context.
            key_value_store: An instance of the `KeyValueStore`. If none is supplied, a new instance will be created.
            state_persistence: An implementation of `StatePersistence` that the task processor can use to retrieve previous copies of the `Task` manifest in order to determine the actions to be performed.

        Returns:
            An updated `KeyValueStore`.

            * Value from the user's input, or the default value if the `waitTimeout` was reached: `task.kind:task.task_id:command:context:RESULT`

        Raises:
            Exception: As determined by the processing logic.
        """
        self.spec = copy.deepcopy(task.spec)
        self.metadata = copy.deepcopy(task.metadata)
        new_key_value_store = KeyValueStore()
        new_key_value_store.store = copy.deepcopy(key_value_store.store)
        log_header = self.format_log_header(task=task, command=command, context=context)
        self.log(message='PROCESSING START', build_log_message_header=False, level='info', header=log_header)
        self.log(message='   spec: {}'.format(json.dumps(self.spec)), build_log_message_header=False, level='debug', header=log_header)
        if '{}:{}:{}:{}:RESULT'.format(task.kind,task.task_id,command,context) in key_value_store.store is True:
            self.log(message='The task have already been processed and will now be ignored. The KeyValueStore will be returned unmodified.', build_log_message_header=False, level='warning', header=log_header)
            return new_key_value_store

        mask_input = False
        default_value = ''
        wait_timeout_seconds = 0
        prompt_text = None
        prompt_char = '> '
        convert_empty_input_to_none_value = False
        # IMPORTANT: Remember that all keys were converted to LOWERCASE
        if 'prompttext' in self.spec:
            if self.spec['prompttext'] is not None:
                if isinstance(self.spec['prompttext'], str):
                    if len(self.spec['prompttext']) > 1 and len(self.spec['prompttext']) < 80:
                        prompt_text = self.spec['prompttext']
        if 'promptcharacter' in self.spec:
            if self.spec['promptcharacter'] is not None:
                if isinstance(self.spec['promptcharacter'], str):
                    if len(self.spec['promptcharacter']) > 0 and len(self.spec['promptcharacter']) < 8:
                        prompt_char = '{} '.format(self.spec['promptcharacter'])
        if 'defaultvalue' in self.spec:
            if self.spec['defaultvalue'] is not None:
                if isinstance(self.spec['defaultvalue'], str):
                    if len(self.spec['defaultvalue']) > 1 and len(self.spec['defaultvalue']) < 256:
                        default_value = self.spec['defaultvalue']
                        prompt_char = '[default={}] {}'.format(default_value, prompt_char)
        if 'maskinput' in self.spec:
            if self.spec['maskinput'] is not None:
                if isinstance(self.spec['maskinput'], bool):
                    mask_input = self.spec['maskinput']
        if 'waittimeoutseconds' in self.spec:
            if self.spec['waittimeoutseconds'] is not None:
                if isinstance(self.spec['waittimeoutseconds'], int):
                    if self.spec['waittimeoutseconds'] > 0 and self.spec['waittimeoutseconds'] < 3600:
                        wait_timeout_seconds = self.spec['waittimeoutseconds']
        if 'convertemptyinputtonone' in self.spec:
            if self.spec['convertemptyinputtonone'] is not None:
                if isinstance(self.spec['convertemptyinputtonone'], bool):
                    convert_empty_input_to_none_value = self.spec['convertemptyinputtonone']
        
        """
            mask_input = False
            default_value = ''
            wait_timeout_seconds = 0
            prompt_text = None
            prompt_char = '> '
            convert_empty_input_to_none_value = False
        """
        self.log(message='FINAL VALUE for mask_input: "{}" (type={})'.format(mask_input, type(mask_input)), build_log_message_header=False, level='debug', header=log_header)
        self.log(message='FINAL VALUE for default_value: "{}" (type={})'.format(default_value, type(default_value)), build_log_message_header=False, level='debug', header=log_header)
        self.log(message='FINAL VALUE for wait_timeout_seconds: "{}" (type={})'.format(wait_timeout_seconds, type(wait_timeout_seconds)), build_log_message_header=False, level='debug', header=log_header)
        self.log(message='FINAL VALUE for prompt_text: "{}" (type={})'.format(prompt_text, type(prompt_text)), build_log_message_header=False, level='debug', header=log_header)
        self.log(message='FINAL VALUE for prompt_char: "{}" (type={})'.format(prompt_char, type(prompt_char)), build_log_message_header=False, level='debug', header=log_header)
        self.log(message='FINAL VALUE for convert_empty_input_to_none_value: "{}" (type={})'.format(convert_empty_input_to_none_value, type(convert_empty_input_to_none_value)), build_log_message_header=False, level='debug', header=log_header)
        
        if prompt_text is not None:
            print('{}\n'.format(prompt_text))

        value = None
        try:
            if wait_timeout_seconds > 0:
                if mask_input is True:
                    value = get_password_input_with_timeout(prompt_char=prompt_char, timeout_seconds=wait_timeout_seconds, default_value=default_value)
                else:
                    value = get_normal_user_input_with_timeout(prompt_char=prompt_char, timeout_seconds=wait_timeout_seconds, default_value=default_value)
            else:
                if mask_input is True:
                    value = getpass(prompt=prompt_char)
                    if value == '':
                        value = default_value
                else:
                    value = input(prompt_char)
                    if value == '':
                        value = default_value
        except:
            self.log(message='EXCEPTION: {}'.format(traceback.format_exc()), build_log_message_header=False, level='error', header=log_header)
            self.log(message='Using DEFAULT value', build_log_message_header=False, level='warning', header=log_header)
            value = default_value
        self.log(message='  Storing value: "{}"'.format(value), build_log_message_header=False, level='info', header=log_header)
        new_key_value_store.save(key='{}:{}:{}:{}:RESULT'.format(task.kind, task.task_id, command, context), value=value)

        self.log(message='value={}'.format(value), build_log_message_header=False, level='debug', header=log_header)
        if value == '' and convert_empty_input_to_none_value is True:
            value = None
        self.log(message='final value={}'.format(value), build_log_message_header=False, level='debug', header=log_header)

        self.spec = dict()
        self.metadata = dict()
        self.log(message='DONE', build_log_message_header=False, level='info', header=log_header)
        self.log(message='  key_value_store keys: {}'.format(list(new_key_value_store.store.keys())), level='debug', build_log_message_header=False, header=log_header)
        return new_key_value_store

