#!/usr/bin/env python3
#
# Copyright 2022 Jonathan L. Komar
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of
# this software and associated documentation files (the "Software"), to deal in
# the Software without restriction, including without limitation the rights to
# use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
# of the Software, and to permit persons to whom the Software is furnished to do
# so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#
import abc
from functools import wraps
from fpinpy.meta.decorators import overrides
from typing import TypeVar, Generic, Callable, List
import sys
# Declare module-scoped type variables for generics
T = TypeVar('T')
U = TypeVar('U')


def functor_law(orig_f):
    @wraps(orig_f)
    def wrapped(*args, **kwargs):
        return orig_f(*args, **kwargs)
    return wrapped

def applicative_law(orig_f):
    @wraps(orig_f)
    def wrapped(*args, **kwargs):
        return orig_f(*args, **kwargs)
    return wrapped

def functional(orig_f):
    @wraps(orig_f)
    def wrapped(*args, **kwargs):
        return orig_f(*args, **kwargs)
    return wrapped

def non_functional_but_useful(orig_f):
    """Represents effects
    """
    @wraps(orig_f)
    def wrapped(*args, **kwargs):
        return orig_f(*args, **kwargs)
    return wrapped

def requires_implementation(deps: List[str]):
    def _requires_implementation(orig_f):
        @wraps(orig_f)
        def wrapped(*args, **kwargs):
            return deps
        return wrapped
    return _requires_implementation

def useful_for_testing(orig_f):
    @wraps(orig_f)
    def wrapped(*args, **kwargs):
        return orig_f(*args, **kwargs)
    return wrapped

"""   
    Ideally, the subclasses of the Result monad would be defined 
    as inner classes of Result, but the Python interpreter does not 
    support this as explained below. To avoid complications, subclasses
    are defined after Result has been fully defined.

    Inner classes may not inherit from their outer classes directly,
    because in Python, the outer class has not yet be fully defined
    at the point of definition of an inner class.
        
    To override the base class, note that
    Object.__dict__ may not be written to if a class inherits directly 
    from Object. 
        
"""

class Result(abc.ABC, Generic[T]):
    """Monad base class.

        This monad supports three modes:
        1. Success
        2. Failure
        3. Empty

        Each mode is enforced by use of factory functions.

        Monadic Laws
        
        1. Kleisli Arrows implemented by flatMap.

        Inherited laws:

        Monoid laws (with respect to functions):

        1. Left identity: ∀ f; (id . f ≡ f) ≡ ((id . f) x ≡ f x) | id=identity and x is any argument
        2. Right identity (dual law/symmetric law): ∀ f; f . id ≡ f | f is any function 
        3. Associativity: f . (g . h) ≡ (f . g) . h | f, g, h are any function

        Functor laws:

        1. Preserves identity: map(id) ≡ id
        2. Preserves composition: map(f . g) ≡ map(f) . map(g)
       
    """

    @classmethod
    def of(cls, value: T, errorMsg: str|None=None, predicate: Callable[[T], bool]=lambda x: True):
        """Main initializer for this class.

            Lifts value into monad.

            A.k.a. unit
        """
        errorMsg = errorMsg if errorMsg != None else "None value"
        try:
            if predicate(value):
                return Result.success(value) if value != None \
                    else Result.failure(errorMsg)
            else:
                return Result.failure(f"{errorMsg}")
        except Exception as e:
            return Result.failure(f"Exception while evaluating predicate: {errorMsg}", exception=e)

    @classmethod
    def success(cls, value: T):
        """Initializer for a Result.Success class.
        """
        return Success(value)
    
    @staticmethod
    def failure(value: T, exception: Exception|None=None):
        """Initializer for a Result.Failure class.

            Supports multiple inputs:
            1. value: str
            2. value: Exception
            3. value: str, exception: Exception
            4. value: Failure[T]

            Note the Python documentation regarding exceptions:

            > Except where mentioned, they have an “associated value” indicating the detailed cause of the error. This may be a string or a tuple of several items of information (e.g., an error code and a string explaining the code). The associated value is usually passed as arguments to the exception class’s constructor.
        """
        if isinstance(exception, Exception):
            #exc_type, exc_obj, exc_tb = sys.exc_info()
            #return Failure(RuntimeError(f"{exception} caught at line {exc_tb.tb_lineno} in file {exc_tb.tb_frame.f_code.co_filename}"))
            return Failure(exception)
        if isinstance(value, Failure):# Failure[T] but isinstance does not support subtypes
            return Failure(value._exception)
        if isinstance(value, str):
            return Failure(RuntimeError(value))
        if isinstance(value, Exception):
            return Failure(value)
        return Failure(RuntimeError(f"You tried to construct  Failure({type(value)}), but that type is not supported."))
    
    @staticmethod
    def empty():
        """Initializer for a Result.Empty class.
        """
        return Empty()

    @staticmethod
    def lift2(func): # -> Result[A] -> Result[B] -> Result[C]
        return lambda result1: lambda result2: result1.map(func).flatMap(lambda x: result2.map(x))

    @staticmethod
    def map2(result1, result2, func): # (Result, Result, func: Result[A] -> Result[B] -> Result[C]) -> Result[C]
        return Result.lift2(func)(result1)(result2)

    def __new__(cls, *args, **kwargs):
        #if str(caller()) != "of":
        #    raise RuntimeError(f'Base class may not be used directly. Prefer Result.of() for instantiatiation. You used {caller()}')
        #assert(kwargs['private_constructor_key'] == Result.__private_constructor_key), \
        #  f'The {cls} class may not be constructed directly. Prefer Result.of() for instantiatiation.'
        instance = object.__new__(cls, args, kwargs)
        return instance

    def __init__(self):
        super().__init__()

    @abc.abstractmethod
    def successValue(self) -> RuntimeError:
        raise NotImplementedError

    @abc.abstractmethod
    def failureValue(self) -> RuntimeError:
        raise NotImplementedError

    @abc.abstractmethod
    def isEmpty(self) -> bool:
        raise NotImplementedError

    @abc.abstractmethod
    def isSuccess(self) -> bool:
        raise NotImplementedError

    @abc.abstractmethod
    def isFailure(self) -> bool:
        raise NotImplementedError
    
    @abc.abstractmethod
    #@functor_law
    def map(self, f: Callable[[T], U]):# -> Result[U]:
        raise NotImplementedError

    @abc.abstractmethod
    #@applicative_law
    def flatMap(self, f):# f: Callable[[T], Result[U]] -> Result[U]:
        raise NotImplementedError

    @abc.abstractmethod
    #@non_functional_but_useful
    def getOrElse(self, default_value) -> T:# default_value: T || Callable[[], T]
        """Supports multiple inputs:

            1. t: T
            2. t: Callable[[], T]
        """
        raise NotImplementedError

    @abc.abstractmethod
    #@non_functional_but_useful
    def getOrThrow(self) -> T:
        raise NotImplementedError
        
    #@functional
    #@requires_implementation([getOrElse, map])
    def orElse(self, default_value: Callable[[], T]):# default_value: Callable[[], Result[T]] -> Result[U]
        return self.map(lambda x: Result.of(x)).getOrElse(default_value)
    
    @abc.abstractmethod
    #@non_functional_but_useful
    def forEach(self, effect: Callable[[T], None]) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    #@non_functional_but_useful
    #@useful_for_testing
    def forEachOrException(self, effect: Callable[[T], None]):# -> Result[RuntimeError]
        raise NotImplementedError

    @abc.abstractmethod
    #@non_functional_but_useful
    #@useful_for_testing
    def forEachOrFail(self, effect: Callable[[T], None]):# -> Result[str]
        raise NotImplementedError

    @abc.abstractmethod
    #@non_functional_but_useful
    def forEachOrThrow(self):# -> Result[Exception]
        raise NotImplementedError

    @abc.abstractmethod
    #@functional
    def mapFailure(self, value: str, exception=RuntimeError):# -> Result[T]
        raise NotImplementedError

    def __str__(self):
        raise NotImplementedError

    def __repr__(self):
        raise NotImplementedError

class Success(Result[T]):
    """Represents a Result that is successful.
    """
    def __new__(cls, *args, **kwargs):
        #if caller() != "success":
        #    raise RuntimeError(f"Prefer Result.of() for instantiatiation.  You used {caller()}.")
        #assert(kwargs['private_constructor_key'] == cls.__private_constructor_key), \
        #  f'The {cls} class may not be constructed directly. Prefer Result.of() for instantiatiation.'
        return object.__new__(cls)

    def __init__(self, value: T):
        self._value = value
        super().__init__()

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return other.successValue() == self.successValue()
        return False

    @overrides(Result)
    def successValue(self):
        return self._value
    
    @overrides(Result)
    def failureValue(self) -> RuntimeError:
        raise RuntimeError(f"Method failureValue() called on a {self.__class__} instance.")

    @overrides(Result)
    def isEmpty(self) -> bool:
        return False
    
    @overrides(Result)
    def isSuccess(self) -> bool:
        return True

    @overrides(Result)
    def isFailure(self) -> bool:
        return False

    @overrides(Result)
    def map(self, f: Callable[[T], U]) -> Result[U]:
        try:
            return Result.success(f(self.successValue()))
        except Exception as e:
            return Result.failure(e)

    @overrides(Result)
    def flatMap(self, f: Callable[[T], Result[U]]) -> Result[U]:
        try:
            return f(self.successValue())
        except Exception as e:
            return Result.failure(e)

    @overrides(Result)
    def getOrElse(self, default_value) -> T:
        return self.successValue()

    @overrides(Result)
    def getOrThrow(self) -> T:
        return self.successValue()

    @overrides(Result)
    def forEach(self, effect: Callable[[T], None]) -> None:
        effect(self.successValue())
        return None

    @overrides(Result)
    def forEachOrException(self, effect: Callable[[T], None]) -> Result[RuntimeError]:
        effect(self.successValue())
        return Result.empty()

    @overrides(Result)
    def forEachOrFail(self, effect: Callable[[T], None]) -> Result[str]:
        effect(self.successValue())
        return Result.empty()

    @overrides(Result)
    def forEachOrThrow(self, effect: Callable[[T], None]) -> None:
        effect(self.successValue())

    @overrides(Result)
    def mapFailure(self, value: str, exception=RuntimeError) -> Result[T]:
        return self

    @overrides(Result)
    def __str__(self):
        return f"Result({self._value})"

    @overrides(Result)
    def __repr__(self):
        return f"Result({repr(self._value)})"

class Empty(Result[T]):
    """Represents a Result that is legitimately empty.
    """
    def __new__(cls, *args, **kwargs):
        #if caller() != "empty":
        #    raise RuntimeError(f"Prefer Result.of() for instantiatiation.  You used {caller()}.")
        #assert(kwargs['private_constructor_key'] == cls.__private_constructor_key), \
        #  f'The {cls} class may not be constructed directly. Prefer Result.of() for instantiatiation.'
        return object.__new__(cls)
    def __init__(self):
        super().__init__() 

    @overrides(Result)
    def successValue(self):
        return RuntimeError(f"Method successValue() called on {self.__class__} instance.")

    @overrides(Result)
    def failureValue(self) -> RuntimeError:
        raise RuntimeError(f"Method failureValue() called on a {self.__class__} instance.")

    @overrides(Result)
    def isEmpty(self) -> bool:
        return True
    
    @overrides(Result)
    def isSuccess(self) -> bool:
        return False

    @overrides(Result)
    def isFailure(self) -> bool:
        return False

    @overrides(Result)
    def map(self, f: Callable[[T], U]):# -> Result[U]: # TODO force Nil to be subclass of Result
        return self

    @overrides(Result)
    def flatMap(self, f: Callable[[T], Result[U]]) -> Result[U]:
        return Result.empty()

    @overrides(Result)
    def getOrElse(self, default_value:T) -> T:
        return default_value() if callable(default_value) else default_value

    @overrides(Result)
    def getOrThrow(self):
        raise RuntimeError(f"getOrThrow called on a {repr(self)}") 

    @overrides(Result)
    def forEach(self, effect: Callable[[T], None]) -> None:
        """Do nothing"""
        return None

    @overrides(Result)
    def forEachOrException(self, effect: Callable[[T], None]) -> Result[Exception]:
        return Result.empty()

    @overrides(Result)
    def forEachOrFail(self, effect: Callable[[T], None]) -> Result[str]:
        return Result.empty()

    @overrides(Result)
    def forEachOrThrow(self, effect: Callable[[T], None]) -> None:
        pass

    @overrides(Result)
    def mapFailure(self, value: str, exception=RuntimeError) -> Result[T]:
        return self

    @overrides(Result)
    def __str__(self):
        return f"Empty()"

    @overrides(Result)
    def __repr__(self):
        return f"Empty()"

class Failure(Empty[T]):
    """Represents a Result that is a failure.
    """
    def __new__(cls, *args, **kwargs):
        #if caller() != "failure":
        #    raise RuntimeError(f"Prefer Result.of() for instantiatiation.  You used {caller()}.")
        #assert(kwargs['private_constructor_key'] == Result.__private_constructor_key), \
        #  f'The {cls} class may not be constructed directly. Prefer Result.of() for instantiatiation.'
        return object.__new__(cls)
    def __init__(self, exception: Exception):
        self._exception = exception
        tmp = sys.exc_info()
        self.exception_type = tmp[0]
        self.exception_object = tmp[1]
        self.exception_traceback = tmp[2]
        super().__init__()
    
    @overrides(Result)
    def successValue(self) -> RuntimeError:
        return RuntimeError(f"Method successValue() called on {self.__class__} instance.")
    
    @overrides(Result)
    def failureValue(self) -> Exception:
        return self._exception

    @overrides(Result)
    def isEmpty(self) -> bool:
        return False
    
    @overrides(Result)
    def isSuccess(self) -> bool:
        return False

    @overrides(Result)
    def isFailure(self) -> bool:
        return True

    @overrides(Result)
    def map(self, f: Callable[[T], U]):# -> Result[U]: TODO: force make Failure subclass of Result
        return self

    @overrides(Result)
    def flatMap(self, f: Callable[[T], Result[U]]):# -> Result[U]:
        return self

    # already implemented in Empty
    #@overrides(Result)
    #def getOrElse(self, default_value) -> U:
    #    return default_value() if callable(default_value) else default_value

    # already implemented in Empty
    #@overrides(Result)
    #def getOrThrow(self, default_value) -> T:

    # already implemented in Empty
    #@overrides(Result)
    #def forEach(self, effect: Callable[[T], None]) -> None:
    #    """Do nothing"""
    #    return None

    @overrides(Result)
    def forEachOrException(self, effect: Callable[[T], Empty[T]]) -> Result[Exception]:
        return Result.success(self._exception)

    @overrides(Result)
    def forEachOrFail(self, effect: Callable[[T], None]) -> Result[str]:
        return Result.success(self._exception)

    @overrides(Result)
    def forEachOrThrow(self, effect: Callable[[T], None]) -> None:
        raise self._exception

    @overrides(Result)
    def mapFailure(self, value: str, exception=RuntimeError) -> Result[T]:
        return Result.failure(value, exception=exception)

    @overrides(Result)
    def __str__(self):
        return f"Failure({self._exception})"

    @overrides(Result)
    def __repr__(self):
        return f"Failure({repr(self._exception)})"
