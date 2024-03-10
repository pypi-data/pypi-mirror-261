"""
The interface for managing the creation of command line argument specifications
and parsing them.

- Author: Casey Walker
- License: MIT

Example usage:
```python
.. include:: ../../examples/say-hello
```
"""

import sys
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Iterable


class Arg_spec(ABC):
    """
    A base class for defining argument types that can be parsed from command
    line arguments.
    """

    def __init__(
        self,
        is_unrestricted: bool = False,
        desc: str = "",
    ):
        """
        # Parameters:
        - `is_unrestricted`:
            Whether or not the argument specification can consume prefixed
            arguments (e.g. it can consume potential floating arguments). This
            is useful for defining a "sink" argument like `"--"`.
        - `desc`:
            The string describing how the argument should be used. This can be
            useful for generating usage documentaion.
        """
        self.is_unrestricted = is_unrestricted
        self.desc = desc

    @abstractmethod
    def can_consume_more(self, prefix: str | None, num_consumed: int) -> bool:
        """
        Return whether the argument specification can consume more arguments
        given a number of arguments that have already been consumed.

        # Parameters:
        - `prefix`:
            The prefix the occurance of the argument was found with. Subclasses
            may find this useful for determining consumption behavior.
        - `num_consumed`:
            The number of arguments that have already been consumed.

        # Returns:
        `True` if more arguments can be consumed, `False` otherwise.
        """

    def consume(
        self, prefix: str | None, consumable_strs: Iterable[str]
    ) -> Iterable[str]:
        """
        Consume arguments from a list of available, consumable arguments.

        # Parameters:
        - `prefix`:
            The prfix the occurance of the argument was found with. Subclasses
            may be able to use this to determine consumption behavior.
        - `consumable_strs`:
            The consumable argument strings to go through.

        # Yields:
        The string that was consumed.

        # Notes:
        Argument specifications are not required to consume all available
        strings, however it is required that returned strings *must* be in order
        in an unbroken chain. In other words, consumed arguments must be
        consecutive without skipping.
        """
        num_consumed = 0
        for arg_str in consumable_strs:
            if not self.can_consume_more(prefix, num_consumed):
                break
            yield arg_str
            num_consumed += 1


class Counting_spec(Arg_spec):
    """
    An argument specification that allows multiple arguments to be consumed.
    This serves as the basis for the typical floating and positional arguments.
    It simply allows for argument consumption based on a count (which may be
    unlimited).
    """

    def __init__(
        self,
        num_args: int,
        is_unbounded: bool = False,
        is_unrestricted: bool = False,
        desc: str = "",
    ):
        """
        # Parameters:
        - `num_args`:
            The number of arguments to consume when the specification is
            encountered. The sign of the number is ignored during consumption,
            but it is preserved so it can used for special purposes if desired.
        - `is_unbounded`:
            Whether or not the specification can consume unlimited arguments.
            This overrides specifying a number of arguments to consume, but the
            information is still preserved in case it's useful post-parsing.
        - `is_unrestricted`:
            Whether or not the specification can consume prefixed arguments.
        - `desc`:
            The description of the argument.

        # Notes:
        Here are a couple ways to use extra information provided by the number
        of arguments and the boundedness of a specification when iterating
        through parsed arguments:
        - One way to use a negative number of arguments is to have it determine
            a maximum number of arguments but allow for fewer. In other words,
            positive means the exact number must be satisfied, but negative
            means fewer are acceptable.
        - Specifying the number of arguments can be combined with unboundedness
            by treating the number of arguments as a minimum number of
            acceptable arguments.
        """
        super().__init__(is_unrestricted=is_unrestricted, desc=desc)
        self.num_args = num_args
        self.is_unbounded = is_unbounded

    def can_consume_more(self, prefix: str | None, num_consumed: int) -> bool:
        if self.is_unbounded:
            return True

        return num_consumed < abs(self.num_args)


class Floating_spec(Counting_spec):
    """
    An optional argument which is prefixed and may be located anywhere in the
    list of arguments (i.e. not positional).

    Floating arguments may have short and long forms, where short forms are
    prefixed by a short prefix and long forms are prefixed by a long prefix.
    Prefixes are determined by the parser. Floating arguments are analagous to
    keyword arguments in programming languages.
    """

    def __init__(
        self,
        short: str | None = None,
        long: str | None = None,
        num_args: int = 0,
        is_unbounded: bool = False,
        is_unrestricted: bool = False,
        desc: str = "",
    ):
        """
        # Parameters:
        - `short`:
            The short form of the specification. May be a string of more than
            one character to allow multiple short strings for the same
            specification. If `None`, no short form will be matched.
        - `long`:
            The long form of the specification. If `None`, no long form will be
            matched.
        - `num_args`:
            The number of arguments to consume.
        - `is_unbounded`:
            Whether or not to consume an unbounded number of arguments.
        - `is_unrestricted`:
            Whether or not to consume prefixed arguments.
        - `desc`:
            The description of the argument.

        # Notes:
        To create a floating argument that only consists of a prefix character
        (e.g. `'-'` or `"--"`), pass `short` and/or `long` as `""` (an empty
        string).
        """
        super().__init__(
            num_args,
            is_unbounded=is_unbounded,
            is_unrestricted=is_unrestricted,
            desc=desc,
        )
        self.short = tuple(short) if short is not None else None
        self.long = long

    def does_str_match_short(self, s: str) -> bool:
        """
        Return if a string matches the specification's short form.
        """
        return s in self.short if self.short is not None else False

    def does_str_match_long(self, s: str) -> bool:
        """
        Return if a string matches the specification's long form.
        """
        return s == self.long if self.long is not None else False

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.short}, {self.long})"


class Positional_spec(Counting_spec):
    """
    A positional argument that occurs in a specific order relative to other
    positional arguments.

    Positional arguments can be interspersed with floating arguments.
    """

    def __init__(
        self,
        name: str | None = None,
        num_args: int = 1,
        is_unbounded: bool = False,
        is_unrestricted: bool = False,
        desc: str = "",
    ):
        """
        # Parameters:
        - `name`:
            The name of the positional argument. This can be useful for
            generating usage documentation.
        - `num_args`:
            The number of arguments to consume for this position. If given as
            `0`, the specification is simply ignored.
        - `is_unbounded`:
            Whether or not to consume an unbounded number of arguments.
        - `is_unrestricted`:
            Whether or not to consume prefixed arguments.
        - `desc`:
            The description of the positional argument, which may be useful for
            generating usage documentation.
        """
        super().__init__(
            num_args,
            is_unbounded=is_unbounded,
            is_unrestricted=is_unrestricted,
            desc=desc,
        )
        self.name = name

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.name})"


@dataclass
class Parsed_arg(object):
    """
    A parsed argument consisting of the various parts it was found with and the
    specification that it was matched with.
    """

    spec: Arg_spec
    """The argument specification that was matched."""

    values: list[str]
    """The associated values that were found for the specification."""

    prefix: str | None = None
    """The prefix that was found if it was floating."""

    floating_form: str | None = None
    """The floating form that was matched if it was floating."""


class Arg_parser(object):
    """
    An argument parser, primarily for parsing command line arguments.
    """

    progname_spec = Positional_spec(
        "Program-name",
        is_unrestricted=True,
        desc="The name by which the program was invokekd.",
    )
    """The specification that captures the program name."""

    unknown_floating_spec = Floating_spec(
        None, None, desc="Unknown floating argument."
    )
    """The specification that captures unknown floating arguments."""

    unknown_positional_spec = Positional_spec(
        "Unknown", desc="Unknown positional argument."
    )
    """The specification that captures extra positional arguments."""

    def __init__(
        self,
        specs: Iterable[Arg_spec],
        progname: str = "",
        short_prefixes: str | None = None,
        long_prefixes: str | Iterable[str] | None = None,
        desc: str = "",
    ):
        """
        # Parameters:
        - `specs`:
            The argument specifications to expect during parsing. Any positional
            specifications present will be ordered as encountered during
            iteration through the specifications.
        - `progname`:
            The name of the program. It may be useful for generating usage
            documentation.
        - `short_prefixes`:
            The prefixes to check for short floating arguments.
        - `long_prefixes`:
            The prefixes to check for long floating arguments.
        - `desc`:
            The description of the program. This may be used in generating usage
            documentation.
        """
        self.special: list[Arg_spec]
        self.floating: list[Floating_spec]
        self.positional: list[Positional_spec]
        self.progname = progname
        self.short_prefixes = (
            list(short_prefixes) if short_prefixes is not None else []
        )
        self.long_prefixes = (
            (
                [long_prefixes]
                if isinstance(long_prefixes, str)
                else (list(long_prefixes))
            )
            if long_prefixes is not None
            else []
        )
        self.desc = desc
        self.__init_specs(specs)

    def __init_specs(self, specs: Iterable[Arg_spec]):
        """
        Initialize the instance's specification lists.

        The lists are sorted into one for positional specifications, one for
        floating specifications, and one for any custom specifications that are
        subclasses of `Arg_spec`. The lists are ordered by order of encounter
        (i.e. the first positional specification that is encountered during
        iteration is appended first, etc.).

        # Parameters:
        - `specs`:
            The argument specifications to sort into respective lists. This
            should be passed directly from `__init__` without modication.

        # Notes:
        This function is meant to extend `__init__` and should thus only ever be
        called once, during instance initialization.
        """
        special: list[Arg_spec] = []
        floating: list[Floating_spec] = []
        positional: list[Positional_spec] = []

        for spec in specs:
            match spec:
                case Floating_spec():
                    floating.append(spec)
                case Positional_spec():
                    positional.append(spec)
                case _:
                    special.append(spec)

        self.special = special
        self.floating = floating
        self.positional = positional

    def is_arg_prefixed(self, arg: str, prefixes: Iterable[str]) -> bool:
        """
        Return whether an argument begins with one of the prefixes.
        """
        return arg.startswith(tuple(prefixes))

    def strip_prefix(
        self, arg: str, prefixes: Iterable[str]
    ) -> tuple[str | None, str]:
        """
        Strip an argument of its prefix.

        # Parameters:
        - `arg`:
            The argument to strip the prefix from.
        - `prefixes`:
            The potential prefixes to strip from the argument.

        # Returns:
        The prefix that was stripped and the stripped argument. If no prefix
        could be stripped, the prefix is returned as `None` and the argument is
        returned unmodifified.
        """
        for prefix in prefixes:
            if arg.startswith(prefix):
                return (prefix, arg.removeprefix(prefix))
        return (None, arg)

    def is_arg_special(self, arg: str, args: Iterable[str]) -> bool:
        """
        Return whether an argument belongs to one of the special specifications
        given during initialization.

        This method is meant to be overridden by subclasses that wish to use
        specially-subclassed versions of `Arg_spec`. Overridden methods should
        return whether an argument is considered to be special or not.

        # Parameters:
        - `arg`:
            The argument to test.
        - `args`:
            The rest of the unparsed arguments. This is given to provide as much
            context as possible to overriding methods that may need more than
            just the argument itself to determine if it is special.

        # Returns:
        `True` if the argument is special, and `False` otherwise. The default
        implementation will always return `False`.
        """
        return False

    def is_arg_floating(self, arg: str) -> bool:
        """
        Return whether an argument begins with one of the prefixes.
        """
        return self.is_arg_prefixed(
            arg, self.short_prefixes + self.long_prefixes
        )

    def find_floating_from_short_form(self, form: str) -> Floating_spec:
        """
        Find the corresponding floating specification that matches a short
        argument.

        # Parameters:
        - `form`:
            The string to match against. It should be stripped of any prefix it
            was found with.

        # Returns:
        The floating specification that matched, or `self.arg_unknown_floating`
        if no match was found.
        """
        for floating_arg in self.floating:
            if floating_arg.does_str_match_short(form):
                return floating_arg
        return self.unknown_floating_spec

    def find_floating_from_long_form(self, form: str) -> Floating_spec:
        """
        Find the corresponding floating specification that matches a long
        argument.

        # Parameters:
        - `form`:
            The string to match against. It should be stripped of any prefix it
            was found with.

        # Returns:
        The floating specification that matched, or `self.arg_unknonw_floating`
        if no match was found.
        """
        for floating_arg in self.floating:
            if floating_arg.does_str_match_long(form):
                return floating_arg
        return self.unknown_floating_spec

    def get_consumable_args(
        self, args: Iterable[str], spec: Arg_spec
    ) -> Iterable[str]:
        """
        Get the list of arguments that can be consumed by a specification.
        """
        for arg in args:
            if not spec.is_unrestricted and self.is_arg_floating(arg):
                break

            yield arg

    def parse_special(
        self,
        arg: str,
        consumable_args: Iterable[str],
    ) -> Iterable[Parsed_arg]:
        """
        Parse a special argument.

        This method is meant to be overridden by subclasses that wish to use it
        for parsing specially-subclassed versions of `Arg_spec`. It is only ever
        called if `is_arg_special` returns `True`.

        # Parameters
        - `arg`:
            The special argument to parse.
        - `consumable_strs`:
            The list of possible arguments that haven't been parsed yet but may
            be consumed by any special specifications used.

        # Yields:
        A parsed argument.

        # Raise:
        - `NotImplementedError` if called without being overridden. Overriding
            methods should *not* raise this or any other exception unless it is
            to serve a similar purpose and require overriding by further
            subclassing.
        """
        raise NotImplementedError()

    def parse_short_floating(
        self, arg: str, args: Iterable[str]
    ) -> Iterable[Parsed_arg]:
        """
        Parse one or more short floating arguments.

        # Parameters
        - `arg`:
            The argument to parse. It should still have the prefix at the
            beginning. It may contain multiple characters corresponding to
            multiple short arguments to be parsed.
        - `args`:
            The current list of remaining arguments that haven't been parsed
            yet.

        # Yields:
        A parsed argument.
        """
        (prefix, short_args) = self.strip_prefix(arg, self.short_prefixes)
        if prefix is None:
            # TODO: return some error or something (this should really be
            #       impossible)
            ...
            return

        args = list(args)
        for short_arg in short_args:
            spec = self.find_floating_from_short_form(short_arg)
            consumable_args = self.get_consumable_args(args, spec)
            values = list(spec.consume(prefix, consumable_args))
            yield Parsed_arg(
                spec, values, prefix=prefix, floating_form=short_arg
            )
            args = args[len(values) :]

    def parse_long_floating(
        self, arg: str, args: Iterable[str]
    ) -> Iterable[Parsed_arg]:
        """
        Parse a long floating argument.

        # Parameters
        - `arg`:
            The argument to parse. It should still have the prefix at the
            beginning.
        - `args`:
            The current list of remaining arguments that haven't been parsed
            yet.

        # Yields:
        A parsed argument.
        """
        (prefix, long_arg) = self.strip_prefix(arg, self.long_prefixes)
        if prefix is None:
            # TODO: return some error or something (this should really be
            #       impossible)
            ...
            return

        spec = self.find_floating_from_long_form(long_arg)
        consumable_args = self.get_consumable_args(args, spec)
        values = list(spec.consume(prefix, consumable_args))
        yield Parsed_arg(spec, values, prefix=prefix, floating_form=long_arg)

    def parse_positional(
        self,
        spec: Positional_spec,
        args: Iterable[str],
    ) -> Iterable[Parsed_arg]:
        """
        Parse a positional argument.

        # Parameters
        - `spec`:
            The positional argument specification to parse for.
        - `args`:
            The list of remaining arguments that haven't been parsed yet.

        # Yields:
        A parsed argument.
        """
        consumable_args = self.get_consumable_args(args, spec)
        values = list(spec.consume(None, consumable_args))
        yield Parsed_arg(spec, values, prefix=None, floating_form=None)

    def parse(self, args: Iterable[str] | None = None) -> Iterable[Parsed_arg]:
        """
        Parse arguments according to the provided specification during
        initialization.

        # Parameters:
        - `args`:
            The list of arguments to parse.

        # Yields:
        A parsed argument.
        """
        if args is None:
            args = sys.argv

        args = list(args)

        for parsed_arg in self.parse_positional(self.progname_spec, args):
            args = args[len(parsed_arg.values) :]
            yield parsed_arg

        positional_iter = iter(self.positional)
        while len(args) > 0:
            arg = args.pop(0)

            parsed_args: Iterable[Parsed_arg]
            if self.is_arg_special(arg, args):
                parsed_args = self.parse_special(arg, args)
            elif self.is_arg_prefixed(arg, self.long_prefixes):
                parsed_args = self.parse_long_floating(arg, args)
            elif self.is_arg_prefixed(arg, self.short_prefixes):
                parsed_args = self.parse_short_floating(arg, args)
            else:
                args = [arg] + args
                spec = next(positional_iter, self.unknown_positional_spec)
                parsed_args = self.parse_positional(spec, args)

            for parsed_arg in parsed_args:
                args = args[len(parsed_arg.values) :]
                yield parsed_arg
