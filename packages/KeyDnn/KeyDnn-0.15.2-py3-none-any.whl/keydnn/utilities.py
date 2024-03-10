from typing import *

import numpy as np

import datetime

import inspect

import base64

import re

from email.mime.multipart import MIMEMultipart 

from email.mime.text import MIMEText 

from email.mime.image import MIMEImage 

import datetime, smtplib

from collections.abc import Iterable as _Iterable

from collections import defaultdict

import textwrap


def bytes2string(bytes : bytes, encoding : str = "ascii") -> str:

    return base64.b64encode(bytes).decode(encoding)

def string2bytes(base64_string : str) -> bytes:

    return base64.b64decode(base64_string)

class OptimizableClass(object):

    DEBUG_MODE = True

    @classmethod
    def optimize(cls) -> None:

        # disable debug mode
        cls.DEBUG_MODE = False

class ComplexFunction(OptimizableClass):

    def __init__(self, function   : Optional[ Callable ] = None,
                       derivative : Optional[ Callable ] = None,
                       inference  : Optional[ Callable ] = None, *,
                       is_average : Optional[ bool ]     = False) -> None:

        if (self.DEBUG_MODE):

            assert ((function is None) or (callable(function)))

            assert ((derivative is None) or (callable(derivative)))

            assert ((inference is None) or (callable(inference)))

            assert ((isinstance(is_average, bool)) or (isinstance(is_average, int)))

        # whether to pass object reference on inference for activation function and its derivative

        self.__function_self_ref   = True

        self.__derivative_self_ref = True

        self.__inference_self_ref  = True

        self.__is_average          = is_average

        # save reference to activation function and its derivative

        self._function   = function

        self._derivative = derivative

        self._inference  = inference

        # setting the object reference flags to False if function specified

        if (self._function is not None):
            self.__function_self_ref = False

        if (self._derivative is not None):
            self.__derivative_self_ref = False

        if (self._inference is not None):
            self.__inference_self_ref = False

    def define_function(self, target_function : Callable) -> None:

        if (self.DEBUG_MODE):
            assert callable(target_function)

        self._function = target_function

    def define_derivative(self, target_function : Callable) -> None:

        if (self.DEBUG_MODE):
            assert callable(target_function)

        self._derivative = target_function

    def define_inference(self, target_function : Callable) -> None:

        if (self.DEBUG_MODE):
            assert callable(target_function)

        self._inference = target_function

    def call_function(self, x : np.ndarray, *args, **kwargs) -> np.ndarray:

        if (self.DEBUG_MODE):
            assert isinstance(x, np.ndarray)

        if (self._function is None):
            raise NotImplementedError("The function has not been defined. Try calling `define_function`.")

        if (self.__function_self_ref):
            return self._function(self, x, *args, **kwargs)

        return self._function(x, *args, **kwargs)

    def call_derivative(self, x : np.ndarray, *args, **kwargs) -> np.ndarray:

        if (self.DEBUG_MODE):
            assert isinstance(x, np.ndarray)

        if (self._derivative is None):
            raise NotImplementedError("The function has not been defined. Try calling `define_derivative`.")

        if (self.__derivative_self_ref):
            return self._derivative(self, x, *args, **kwargs)

        return self._derivative(x, *args, **kwargs)

    def call_inference(self, x : np.ndarray, *args, **kwargs) -> np.ndarray:

        if (self.DEBUG_MODE):
            assert isinstance(x, np.ndarray)

        if (self._inference is None):
            raise NotImplementedError("The function has not been defined. Try calling `define_inference`.")

        if (self.__inference_self_ref):
            return self._inference(self, x, *args, **kwargs)

        return self._inference(x, *args, **kwargs)
    
    def merge_losses(self, losses        : Iterable[ Union[ float, int ] ], 
                           sample_counts : Iterable[ int ]
            
            ) -> Tuple[ float, int ]:

        if (self.DEBUG_MODE):

            assert ((isinstance(losses, list)) or (isinstance(losses, tuple)) or (isinstance(losses, np.ndarray)))

            assert ((isinstance(sample_counts, list)) or (isinstance(sample_counts, tuple)) or (isinstance(sample_counts, np.ndarray)))

            assert (len(losses) == len(sample_counts))

        total_samples = int(np.sum(sample_counts))

        if (self.__is_average):
            return (float(np.dot(losses, sample_counts) / total_samples), total_samples)
        
        return (float(np.sum(losses)), total_samples)

    def __call__(self, x : np.ndarray, *args, **kwargs) -> np.ndarray:

        if (self.DEBUG_MODE):
            assert isinstance(x, np.ndarray)

        return self.call_inference(x, *args, **kwargs)
    

class NetworkLayer(OptimizableClass):
    pass

class NeuralNetwork(OptimizableClass):

    NETWORK_LAYERS = {}

    @classmethod
    def register_layer(cls, layer_class : Type[ "NetworkLayer" ]) -> Type[ "NetworkLayer" ]:

        cls.NETWORK_LAYERS[layer_class.__name__] = layer_class

        return layer_class
    
def batch_one_hot_encode(indices : np.ndarray, num_classes : Optional[ int ] = 10) -> np.ndarray:

    batch_size : int = len(indices)

    encoded_matrix : np.ndarray = np.zeros((batch_size, num_classes))

    for i in range(batch_size):
        encoded_matrix[i, indices[i]] = 1

    return encoded_matrix

def catch_error(default_value : Optional[ Any ] = None, ignore : Optional[ List[ Exception ] ] = []) -> Callable:

    ignore_tuple : Exception = tuple([  KeyboardInterrupt, *ignore  ])

    def _catch_error(function : Callable) -> Callable:

        def __catch_error(*args, **kwargs) -> Any:

            try:
                return function(*args, **kwargs)

            except ignore_tuple:
                raise

            except Exception:
                return default_value
            
        return __catch_error
    
    return _catch_error

def initialize_weights(target_size : tuple, n_input_nodes : int) -> np.ndarray:
    return np.random.randn(*target_size).reshape(target_size) * np.sqrt(2.0 / n_input_nodes)

class NeoVisUtils(object):

    SAFE_MODE = True

    @classmethod
    def apply_filter_condition(cls, f_query_string : str, condition : Dict[ str, str ]) -> str:

        if (cls.SAFE_MODE):

            assert isinstance(f_query_string, str)

            assert isinstance(condition, dict)

        return f_query_string.format(f"""{{{  ",".join(map(lambda x : f"{x[0]}: {repr(x[1])}", condition.items()))  }}}""")

    @classmethod
    def create_node_query_string(cls, counter : int, query_data : List[ Dict[ str, str ] ]) -> str:

        if (cls.SAFE_MODE):

            assert isinstance(counter, int)

            assert isinstance(query_data, list)

        if (counter == 1):
            return f"p{counter} = (n{counter}: `{query_data[counter-1][0]}`{{}})"

        return f"p{counter} = (n{counter}) - [r{counter}] -> (n{counter}: `{query_data[counter-1][0]}`{{}})"

    @classmethod
    def format_query(cls, query_data : List[ Dict[ str, str ] ]) -> str:

        if (cls.SAFE_MODE):
            assert isinstance(query_data, list)

        query_string = cls.apply_filter_condition(f"MATCH {cls.create_node_query_string(1, query_data)}", query_data[0][1])

        for counter in range(2, len(query_data) + 1):
            query_string += cls.apply_filter_condition(f" OPTIONAL MATCH p{counter} = (n{counter-1}) - [r{counter-1}] -> (n{counter}: `{query_data[counter-1][0]}`{{}})", query_data[counter-1][1])

        query_string += " RETURN " + ", ".join(f"p{counter}" for counter in range(1, len(query_data) + 1))

        return query_string

epsilon = 1e-7

class ChineseDigitsConverter(object):

    SINGLE_DIGITS = "零一二三四五六七八九"

    DIGIT_UNITS = "十百千萬億兆"

    SINGLE_DIGITS_MAP = {
        "零" : 0,
        "一" : 1,
        "二" : 2,
        "三" : 3,
        "四" : 4,
        "五" : 5,
        "六" : 6,
        "七" : 7,
        "八" : 8,
        "九" : 9,
        "兩" : 2
    }

    UNITS_WEIGHTS = [
        10, 100, 1_000, 10_000, 100_000_000, 1_000_000_000_000
    ]

    @staticmethod
    def find_number_clusters(int_array : List[ int ]) -> List[ int ]:

        indices = []
        
        cur_idx = 0
        
        num_idx = len(int_array)

        while (cur_idx < num_idx):
            
            max_idx = max(range(cur_idx, num_idx), key = int_array.__getitem__)

            indices.append(max_idx)

            cur_idx = max_idx + 1

        return indices 

    @classmethod
    def _zh2no(cls, word : str) -> str:
        return "".join(map(lambda x : str(cls.SINGLE_DIGITS.index(x)), word))

    @classmethod
    def _convert_to_integer(cls, string_list : List[ str ]) -> int:

        last_item = string_list[-1]

        if (len(last_item) == 1):
            
            if (cls.DIGIT_UNITS.__contains__(last_item)):
                multiplier = cls.UNITS_WEIGHTS[cls.DIGIT_UNITS.index(last_item)]
                last_digit = -1

            else:
                multiplier = 1
                last_digit = cls.SINGLE_DIGITS_MAP[last_item]

        else:

            multiplier = cls.UNITS_WEIGHTS[cls.DIGIT_UNITS.index(last_item[1])]

            last_digit = cls.SINGLE_DIGITS_MAP[last_item[0]]

        accumulation = 0

        for string in string_list[:-1]:

            if ((len(string) == 1) and (string == "零")):
                continue

            digit, units = cls.SINGLE_DIGITS_MAP[string[0]], cls.UNITS_WEIGHTS[cls.DIGIT_UNITS.index(string[1])]

            accumulation += (digit * units)

        return multiplier * ((accumulation + last_digit) if (last_digit != -1) else max(1, accumulation))

    @classmethod
    def _process(cls, word : str) -> str:

        tokens = list(filter("".__ne__, re.findall(f"[{cls.SINGLE_DIGITS}兩]?[{cls.DIGIT_UNITS}]?", word)))

        unit_indices = [
            ((cls.DIGIT_UNITS.index(x[-1])) if (cls.DIGIT_UNITS.__contains__(x[-1])) else (-2))
                for x in tokens
        ]

        clusters = cls.find_number_clusters(unit_indices)

        accumulation = 0

        for idx, start_idx in enumerate(clusters):

            actual_start_idx = ((0) if (idx == 0) else (clusters[idx-1] + 1))

            accumulation += cls._convert_to_integer(tokens[actual_start_idx:start_idx+1])

        return str(accumulation)

    @classmethod
    def chinese_to_arabic(cls, sentence : str) -> str:

        assert isinstance(sentence, str)

        patt = f"[{cls.SINGLE_DIGITS}{cls.DIGIT_UNITS}兩]+"
        
        tokens = re.findall(f"{patt}|[^{cls.SINGLE_DIGITS}{cls.DIGIT_UNITS}兩]+", sentence)

        converted_tokens = []

        for token in tokens:

            if all(cls.SINGLE_DIGITS.__contains__(char) for char in token):
                converted_tokens.append(cls._zh2no(token))
                continue

            if (re.match(patt, token) is None):
                converted_tokens.append(token)
                continue

            converted_tokens.append(cls._process(token))

        return "".join(converted_tokens)
    
def type_error_check(variable : Any, type_list : List[ Union[ Type, None ] ]) -> bool:

    if ((type_list.__contains__(None)) and (variable is None)):
        return False

    if ((any((__variable is callable) for __variable in type_list)) and (callable(variable))):
        return False

    for var_type in type_list:

        if ((var_type is None) or (var_type is callable)):
            continue 

        if (isinstance(variable, var_type)):
            return False

    return True

class VariableTypeError(TypeError):

    def __init__(self, variable : Any, var_name : str, type_list : List[ Union[ Type, None ] ]) -> None:

        error_message = f"Variable {repr(var_name)} should be"

        for var_type in type_list:

            if (var_type is None):
                error_message += " None,"

            elif (var_type is callable):
                error_message += " callable,"

            else:
                error_message += f" {repr(var_type)},"

        super(VariableTypeError, self).__init__(error_message[:-1] + ".")

def save_parameters(private_level : Optional[ int ] = 0) -> Callable:

    if (type_error_check(private_level, [ int ])):
        raise VariableTypeError(private_level, "private_level", [ int ])

    if (private_level < 0):
        raise ValueError(f"""Parameter `private_level` cannot be a negative number.""")

    def get_default_args(function : Callable) -> Dict[ str, any ]:

        return {
            key : val.default 
                for key, val in inspect.signature(function).parameters.items()
                    if val.default is not inspect.Parameter.empty
        }

    def _set_variables(self, init_function : Callable, *args, **kwargs) -> None:

        nonlocal private_level, get_default_args

        class_prefix = ((f"_{self.__class__.__name__}") if (private_level >= 2) else (""))

        prefix = "_" * private_level

        for key, val in get_default_args(init_function).items():
            setattr(self, f"""{class_prefix}{prefix}{key}""", val)

        for key, val in kwargs.items():
            setattr(self, f"""{class_prefix}{prefix}{key}""", val)

        for key, val in zip(init_function.__code__.co_varnames[1:], args):
            setattr(self, f"""{class_prefix}{prefix}{key}""", val)

    def _save_parameters(init_function : Callable) -> Callable:

        nonlocal _set_variables

        if (type_error_check(init_function, [ callable ])):
            raise VariableTypeError(init_function, "init_function", [ callable ])

        def __save_parameters(self, *args, **kwargs) -> None:

            nonlocal _set_variables, init_function

            _set_variables(self, init_function, *args, **kwargs)

            init_function(self, *args, **kwargs)

        return __save_parameters

    return _save_parameters

class KeyResponse(dict):

    def __check_type(self) -> None:

        if (type_error_check(self.__status, [ bool ])):
            raise VariableTypeError(self.__status, "status", [ bool ])

        if (type_error_check(self.__info, [ str ])):
            raise VariableTypeError(self.__info, "info", [ str ])

    @save_parameters(2)
    def __init__(self, status : bool, message : Any, info : Optional[ str ] = "", **kwargs) -> None:

        super(KeyResponse, self).__init__()

        self.__check_type()

        self.update({
            "status"  : status,
            "message" : message
        })

        if (info != ""):
            self.__setitem__("info", info)

        self.update(kwargs)

class TimeStamp(object):


    TIMESTAMP_FORMAT = "%Y-%m-%d_%H:%M:%S"


    @staticmethod
    def current_time(timezone : Optional[ datetime.timezone ] = None) -> datetime.datetime:

        if (type_error_check(timezone, [ datetime.timezone, None ])):
            raise VariableTypeError(timezone, "timezone", [ datetime.timezone, None ])
        
        if (timezone is None):
            timezone = datetime.timezone.utc

        return datetime.datetime.now(timezone)
    

    @classmethod
    def loads_time(cls, timestamp : str) -> datetime.datetime:

        if (type_error_check(timestamp, [ str ])):
            raise VariableTypeError(timestamp, "timestamp", [ str ])
        
        return datetime.datetime.strptime(timestamp, cls.TIMESTAMP_FORMAT)
    

    @classmethod
    def dumps_time(cls, timestamp : datetime.datetime) -> str:

        if (type_error_check(timestamp, [ datetime.datetime ])):
            raise VariableTypeError(timestamp, "timestamp", [ datetime.datetime ])
        
        return timestamp.strftime(cls.TIMESTAMP_FORMAT)


class SimpleGmailSender(object):

    HOST_GMAIL = "smtp.gmail.com"

    PORT_GMAIL = "587"

    VERBOSE    = 0

    @save_parameters()
    def __init__(self, username : str, 
                       password : str) -> None:
        
        if (type_error_check(username, [ str ])):
            raise VariableTypeError(username, "username", [ str ])
        
        if (type_error_check(password, [ str ])):
            raise VariableTypeError(password, "password", [ str ])

    def __enter__(self) -> None:
        return self 
    
    def __exit__(self, *args, **kwargs) -> None:
        pass 

    @staticmethod 
    def _init_mime_container(receiver   : str, 
                             sender     : str, 
                             subject    : str, 
                             content    : str, 
                             image_data : bytes = None) -> MIMEMultipart:
        
        if (type_error_check(receiver, [ str ])):
            raise VariableTypeError(receiver, "receiver", [ str ])
        
        if (type_error_check(sender, [ str ])):
            raise VariableTypeError(sender, "sender", [ str ])
        
        if (type_error_check(subject, [ str ])):
            raise VariableTypeError(subject, "subject", [ str ])
        
        if (type_error_check(content, [ str ])):
            raise VariableTypeError(content, "content", [ str ])
        
        if (type_error_check(image_data, [ bytes, None ])):
            raise VariableTypeError(image_data, "image_data", [ bytes, None ])
        
        container = MIMEMultipart()

        container["subject"] = subject 

        container["from"] = sender 

        container["to"] = receiver 

        container.attach(MIMEText(content))

        if (image_data is not None):
            container.attach(MIMEImage(image_data))

        return container 
    
    def send(self, receiver   : str, 
                   subject    : str, 
                   content    : str, 
                   image_data : bytes = None) -> bool:
        
        if (type_error_check(receiver, [ str ])):
            raise VariableTypeError(receiver, "receiver", [ str ])
        
        if (type_error_check(subject, [ str ])):
            raise VariableTypeError(subject, "subject", [ str ])
        
        if (type_error_check(content, [ str ])):
            raise VariableTypeError(content, "content", [ str ])
        
        if (type_error_check(image_data, [ bytes, None ])):
            raise VariableTypeError(image_data, "image_data", [ bytes, None ])
        
        with smtplib.SMTP(host = self.HOST_GMAIL, port = self.PORT_GMAIL) as smtp:

            try:

                smtp.ehlo()

                smtp.starttls()

                smtp.login(self.username, self.password)

                smtp.send_message(self._init_mime_container(
                    receiver, self.username, subject, content, image_data
                ))

                return True 
            
            except KeyboardInterrupt:
                raise

            except Exception as errorMessage:
                if (self.VERBOSE):
                    print(errorMessage)

        return False 

MAP_SAFE = True

def cmap(map_function  : Callable, 
         iterable      : Iterable, 
         cond_function : Optional[ Callable ] = None
        ) -> Iterator:

    """
        Description:
            This function performs conditional mapping for iterators.

        Parameters:
            [ 1 ] map_function  : Callable[ <arg> ]
            [ 2 ] iterable      : Iterable
            [ 3 ] cond_function : Callable[ <arg> ]

        Returns:
            [ R ] iterable      : Iterable
    """

    global MAP_SAFE

    if (MAP_SAFE):

        if (type_error_check(map_function, [ callable ])):
            raise VariableTypeError(map_function, "map_function", [ callable ])

        if (type_error_check(iterable, [ _Iterable ])):
            raise VariableTypeError(iterable, "iterable", [ _Iterable ])

        if (type_error_check(cond_function, [ callable, None ])):
            raise VariableTypeError(cond_function, "cond_function", [ callable, None ])

    if (cond_function is None):
        return (map_function(x) for x in iterable)

    return (((map_function(x)) if (cond_function(x)) else (x)) for x in iterable)

def dmap(map_function : Callable, 
         dictionary   : Dict, 
         key_names    : Optional[ Iterable ] = None
        ) -> Dict:

    """
        Description:
            This function performs conditional dictionary mapping.

        Parameters:
            [ 1 ] map_function : Callable[ <arg1: key>, <arg2: val> ]
            [ 2 ] dictionary   : Dict
            [ 3 ] key_names    : Iterable

        Returns:
            [ R ] dictionary   : Dict
    """

    global MAP_SAFE

    if (MAP_SAFE):

        if (type_error_check(map_function, [ callable ])):
            raise VariableTypeError(map_function, "map_function", [ callable ])

        if (type_error_check(dictionary, [ dict ])):
            raise VariableTypeError(dictionary, "dictionary", [ dict ])

        if (type_error_check(key_names, [ _Iterable, None ])):
            raise VariableTypeError(key_names, "key_names", [ _Iterable, None ])

    if (key_names is None):
        for key, val in dictionary.items():
            dictionary[key] = map_function(key, val)
        return dictionary

    if (type_error_check(key_names, [ set ])):
        key_names = set(key_names)
        
    for key, val in dictionary.items():
        if (key_names.__contains__(key)):
            dictionary[key] = map_function(key, val)
    
    return dictionary

# class FunctionSimplifier(object):

#     _function_mapping : Dict[ int, Callable ] = defaultdict(dict)

#     _function_counter : int = 0

#     MACRO_START : str = '""">>function-simplifier>>"""'

#     MACRO_END   : str = '"""<<function-simplifier<<"""'

#     DEFAULT_LABEL : int = 0

#     @classmethod
#     def define_macro_symbols(cls, open_symbol  : str,
#                                   close_symbol : str) -> None:

#         if (type_error_check(open_symbol, [ str ])):
#             raise VariableTypeError(open_symbol, "open_symbol", [ str ])

#         if (type_error_check(close_symbol, [ str ])):
#             raise VariableTypeError(close_symbol, "close_symbol", [ str ])

#         cls.MACRO_START = open_symbol

#         cls.MACRO_END = close_symbol

#     @classmethod
#     def conditional_simplify(cls, label : Optional[ int ] = DEFAULT_LABEL) -> Callable:

#         if (type_error_check(label, [ int ])):
#             raise VariableTypeError(label, "label", [ int ])

#         def _conditional_simplify(source_function : Callable) -> Callable:

#             cls._function_mapping[label][cls._function_counter] = source_function

#             counter : int = cls._function_counter

#             def formatted_function(*args, **kwargs) -> Any:
#                 return cls._function_mapping[label][counter](*args, **kwargs)

#             cls._function_counter += 1

#             return formatted_function

#         return _conditional_simplify

#     @classmethod
#     def simplify(cls, labels : Union[ set, list, tuple, int, None ] = None) -> None:

#         if (type_error_check(labels, [ set, list, tuple, int, None ])):
#             raise VariableTypeError(labels, "labels", [ set, list, tuple, int, None ])

#         if (labels is None):
#             labels = tuple(cls._function_mapping.keys())

#         elif (isinstance(labels, int)):
#             labels = (labels, )

#         @catch_error(False, [ KeyboardInterrupt ])
#         def _safe_execute(label, counter) -> bool:

#             formatted_code = re.sub(f"""{cls.MACRO_START}[^.]*{cls.MACRO_END}""", "", textwrap.dedent(inspect.getsource(cls._function_mapping[label][counter])))

#             exec(formatted_code)

#             cls._function_mapping[label][counter] = locals()[cls._function_mapping[label][counter].__name__]

#             return True

#         for label in labels:
#             for counter in list(cls._function_mapping[label].keys()):
#                 if (_safe_execute(label, counter)):
#                     continue
#                 del cls._function_mapping[label][counter]
#                 if (len(cls._function_mapping[label]) == 0):
#                     del cls._function_mapping[label]

class SimpleMethod(object):


    _LABELS_TO_SIMPLIFY : set                                              = set()

    _FUNCTION_COUNTER   : int                                              = 0

    _FUNCTION_CONTEXT   : Dict[ int, List[ dict ] ]                        = defaultdict(list) # { <key> : [ <global_dict>, <local_dict> ] }

    _FUNCTION_EXECUTE   : Dict[ Union[ int, str ], Dict[ int, callable ] ] = defaultdict(dict)

    _FUNCTION_CODESRC   : Dict[ Union[ int, str ], Dict[ int, str ] ]      = defaultdict(dict)

    _FUNCTION_FORMATTED : Dict[ Union[ int, str ], Dict[ int, bool ] ]     = defaultdict(dict)


    _TAG_OPEN  = [ "# >> FS-{}", "# >> F-{}-S-{}" ]

    _TAG_CLOSE = [ "# << FS-{}", "# << F-{}-S-{}" ]


    @classmethod
    def add_labels(cls, label : int) -> None:

        if (type_error_check(label, [ int ])):
            raise VariableTypeError(label, "label", [ int ])

        if (label in cls._LABELS_TO_SIMPLIFY):
            return

        cls._LABELS_TO_SIMPLIFY.add(label)

        cls._simplify_functions(label)

    @classmethod
    def __remove_hidden_sections(cls, text : str, label : int) -> str:

        (S, E) = (1, 1)

        while (len(re.findall(cls._TAG_OPEN[0].format(repr(label)), text))):
            text = re.sub(cls._TAG_OPEN[0].format(repr(label)), cls._TAG_OPEN[1].format(S, repr(label)), text, count = 1)
            S += 1

        while (len(re.findall(cls._TAG_CLOSE[0].format(repr(label)), text))):
            text = re.sub(cls._TAG_CLOSE[0].format(repr(label)), cls._TAG_CLOSE[1].format(E, repr(label)), text, count = 1)
            E += 1

        if (S != E):
            raise ValueError("Number of opening and closing tags should match and not nested.")

        for i in range(1, E + 1):
            text = re.sub(f"""[^\n]*{cls._TAG_OPEN[1].format(i, repr(label))}[\d\D]*{cls._TAG_CLOSE[1].format(i, repr(label))}[^\n]*\n""", "", text)

        return text

    @classmethod
    def _simplify_functions(cls, labels : Union[ int, set, list, tuple, None ] = None) -> None:

        if (type_error_check(labels, [ int, set, list, tuple, None ])):
            raise VariableTypeError(labels, "labels", [ int, set, list, tuple, None ])

        if not (type_error_check(labels, [ int ])):
            labels = (labels, )

        elif (labels is None):
            labels = tuple(cls._FUNCTION_CODESRC.keys())

        for label in labels:

            for counter in tuple(cls._FUNCTION_CODESRC[label].keys()):

                if (cls._FUNCTION_FORMATTED[label][counter]):
                    continue

                code_source : str = cls._FUNCTION_CODESRC[label][counter]

                # print(code_source)

                (function_name_original, function_name_formatted) = (
                    cls._FUNCTION_EXECUTE[label][counter].__name__,
                    f"""{cls._FUNCTION_EXECUTE[label][counter].__name__}_FS_REDEFINED_{label}_{counter}"""
                )

                # context_decorator_removed : str = re.sub(f"""[^\n]*@{cls.__name__}.capture_context\((.*)\)\n""", "", code_source)

                # context_decorator_removed : str = re.sub(f"""[^\n]*@classmethod(.*)\n""", "", context_decorator_removed)

                # context_decorator_removed : str = re.sub(f"""[^\n]*@(.*)\n""", "", context_decorator_removed)

                context_decorator_removed : str = re.sub(f"""^[\d\D]*@{cls.__name__}.capture_context\((.*)\)\ndef {function_name_original}""", f"\ndef {function_name_original}", code_source, count = 1)

                # print(context_decorator_removed)


                # (function_name_original, function_name_formatted) = (
                #     cls._FUNCTION_EXECUTE[label][counter].__name__,
                #     f"""{cls._FUNCTION_EXECUTE[label][counter].__name__}_FS_REDEFINED_{label}_{counter}"""
                # )

                function_renamed : str = re.sub(f"{function_name_original}\(", f"{function_name_formatted}(", context_decorator_removed)

                # print(function_renamed)

                hidden_section_removed : str = cls.__remove_hidden_sections(function_renamed, label)

                # print(hidden_section_removed)

                cls._FUNCTION_CONTEXT[counter][1].update({
                    function_name_formatted : None
                })

                exec(hidden_section_removed, cls._FUNCTION_CONTEXT[counter][0], cls._FUNCTION_CONTEXT[counter][1])

                cls._FUNCTION_EXECUTE[label][counter] = cls._FUNCTION_CONTEXT[counter][function_name_formatted in cls._FUNCTION_CONTEXT[counter][1]][function_name_formatted]

                cls._FUNCTION_FORMATTED[label][counter] = True


    @classmethod
    def capture_context(cls, function_label : int, 
                             global_context : dict, 
                             local_context  : dict
                ) -> Callable:

        if (type_error_check(function_label, [ int ])):
            raise VariableTypeError(function_label, "function_label", [ int ])

        if (type_error_check(global_context, [ dict ])):
            raise VariableTypeError(global_context, "global_context", [ dict ])

        if (type_error_check(local_context, [ dict ])):
            raise VariableTypeError(local_context, "local_context", [ dict ])

        def _capture_context(function : Callable) -> Callable:

            if (type_error_check(function, [ callable ])):
                raise VariableTypeError(function, "function", [ callable ])

            current_counter_index : int = cls._FUNCTION_COUNTER

            cls._FUNCTION_COUNTER += 1

            cls._FUNCTION_CONTEXT[current_counter_index].append(global_context)

            cls._FUNCTION_CONTEXT[current_counter_index].append(local_context)

            cls._FUNCTION_EXECUTE[function_label][current_counter_index] = function

            try:
                cls._FUNCTION_CODESRC[function_label][current_counter_index] = textwrap.dedent(inspect.getsource(function))
            except OSError:
                raise SyntaxError(f"You cannot use the `capture_context` decorator in a nested fashion.")

            cls._FUNCTION_FORMATTED[function_label][current_counter_index] = False

            def execute_function(*args, **kwargs) -> Any:
                return cls._FUNCTION_EXECUTE[function_label][current_counter_index](*args, **kwargs)

            if (function_label in cls._LABELS_TO_SIMPLIFY):
                cls._simplify_functions(function_label)

            return execute_function

        return _capture_context


if (__name__ == "__main__"):

    # @catch_error()
    # def parse_int(string : str) -> int:
    #     return int(string)
    
    # print(parse_int("123"))

    # print(parse_int("2-3"))

    # @FunctionSimplifier.conditional_simplify(1)
    # def add_numbers_1(val1 : int, val2 : int) -> int:

    #     val = 0

    #     """>>function-simplifier>>"""

    #     val = 1000 + val1 + val2

    #     """<<function-simplifier<<"""

    #     val = val + val1 + val2

    #     return val

    # @FunctionSimplifier.conditional_simplify(2)
    # def add_numbers_2(val1 : int, val2 : int) -> int:

    #     val = 0

    #     """>>function-simplifier>>"""

    #     val = 1000 + val1 + val2

    #     """<<function-simplifier<<"""

    #     val = val + val1 + val2

    #     return val

    # print(add_numbers_1(12, 28))

    # print(add_numbers_2(12, 28))

    # FunctionSimplifier.simplify([1, 2])

    # print(add_numbers_1(12, 28))

    # print(add_numbers_2(12, 28))

    # FunctionSimplifier.define_macro_symbols('""">>FS"""', '"""<<FS"""')

    # @FunctionSimplifier.conditional_simplify(1207)
    # def multiply(val1 : int, val2 : int) -> int:

    #     """>>FS"""

    #     print("OKAY")

    #     """<<FS"""

    #     return val1 * val2

    # print(multiply(12, 13))

    # print(id(multiply))

    # FunctionSimplifier.simplify(1207)

    # print(multiply(12, 13))

    # print(id(multiply))

    @SimpleMethod.capture_context(127, globals(), locals())
    def add_numbers_1(val1 : int, val2 : int) -> int:

        val = 0

        # >> FS-127

        val = 1000 + val1 + val2

        # << FS-127

        val = val + val1 + val2

        return val

    @SimpleMethod.capture_context(1207, globals(), locals())
    def add_numbers_2(val1 : int, val2 : int) -> int:

        val = 0

        # >> FS-1207

        val = 1000 + val1 + val2

        # << FS-1207

        val = val + val1 + val2

        return val

    print(add_numbers_1(12, 28))

    print(add_numbers_2(12, 28))

    SimpleMethod.add_labels(127)

    SimpleMethod.add_labels(1207)

    print(add_numbers_1(12, 28))

    print(add_numbers_2(12, 28))
