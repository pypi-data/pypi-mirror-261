"""Custom spaCy attributes for spaczz."""
import typing as ty
import warnings

from spacy.tokens import Doc
from spacy.tokens import Span
from spacy.tokens import Token

from .customtypes import SpaczzType
from .exceptions import AttrOverwriteWarning


class SpaczzAttrs:
    """Adds spaczz custom attributes to spaCy."""

    _initialized = False

    @classmethod
    def initialize(cls: ty.Type["SpaczzAttrs"]) -> None:
        """Initializes and registers custom attributes."""
        if not cls._initialized:
            try:
                Token.set_extension("spaczz_token", default=False)
                Token.set_extension("spaczz_type", default=None)
                Token.set_extension("spaczz_ratio", default=None)
                Token.set_extension("spaczz_pattern", default=None)

                Span.set_extension("spaczz_ent", getter=cls.get_spaczz_ent)
                Span.set_extension("spaczz_type", getter=cls.get_span_type)
                Span.set_extension("spaczz_types", getter=cls.get_span_types)
                Span.set_extension("spaczz_ratio", getter=cls.get_ratio)
                Span.set_extension("spaczz_pattern", getter=cls.get_pattern)

                Doc.set_extension("spaczz_doc", getter=cls.get_spaczz_doc)
                Doc.set_extension("spaczz_types", getter=cls.get_doc_types)
                cls._initialized = True
            except ValueError:
                warnings.warn(
                    """One or more spaczz custom extensions has already been registered.
                    These are being force overwritten. Please avoid defining personal,
                    custom extensions prepended with `"spaczz_"`.
                """,
                    AttrOverwriteWarning,
                    stacklevel=2,
                )
                Token.set_extension("spaczz_token", default=False, force=True)
                Token.set_extension("spaczz_type", default=None, force=True)
                Token.set_extension("spaczz_ratio", default=None, force=True)

                Span.set_extension("spaczz_type", getter=cls.get_span_type, force=True)
                Span.set_extension(
                    "spaczz_types", getter=cls.get_span_types, force=True
                )
                Span.set_extension("spaczz_ratio", getter=cls.get_ratio, force=True)
                Span.set_extension("spaczz_pattern", getter=cls.get_pattern, force=True)

                Doc.set_extension("spaczz_doc", getter=cls.get_spaczz_doc, force=True)
                Doc.set_extension("spaczz_types", getter=cls.get_doc_types, force=True)

    @staticmethod
    def get_spaczz_ent(span: Span) -> bool:
        """Getter for spaczz_ent `Span` attribute."""
        return all([token._.spaczz_token for token in span])

    @classmethod
    def get_span_type(
        cls: ty.Type["SpaczzAttrs"], span: Span
    ) -> ty.Optional[SpaczzType]:
        """Getter for spaczz_type `Span` attribute."""
        if cls._all_equal([token._.spaczz_type for token in span]):
            return span[0]._.spaczz_type
        else:
            return None

    @staticmethod
    def get_span_types(span: Span) -> ty.Set[SpaczzType]:
        """Getter for spaczz_types `Span` attribute."""
        types = [token._.spaczz_type for token in span if token._.spaczz_type]
        return set(types)

    @classmethod
    def get_ratio(cls: ty.Type["SpaczzAttrs"], span: Span) -> ty.Optional[int]:
        """Getter for spaczz_ratio `Span` attribute."""
        if cls._all_equal([token._.spaczz_ratio for token in span]):
            return span[0]._.spaczz_ratio
        else:
            return None

    @classmethod
    def get_pattern(cls: ty.Type["SpaczzAttrs"], span: Span) -> ty.Optional[str]:
        """Getter for spaczz_pattern `Span` attribute."""
        if cls._all_equal([token._.spaczz_pattern for token in span]):
            return span[0]._.spaczz_pattern
        else:
            return None

    @staticmethod
    def get_spaczz_doc(doc: Doc) -> bool:
        """Getter for spaczz_doc `Doc` attribute."""
        return any([token._.spaczz_token for token in doc])

    @staticmethod
    def get_doc_types(doc: Doc) -> ty.Set[SpaczzType]:
        """Getter for spaczz_types `Doc` attribute."""
        types = [token._.spaczz_type for token in doc if token._.spaczz_type]
        return set(types)

    @staticmethod
    def _all_equal(iterable: ty.Iterable[ty.Any]) -> bool:
        """Tests if all elements of iterable are equal."""
        iterator = iter(iterable)
        try:
            first = next(iterator)
        except StopIteration:
            return True
        return all(first == rest for rest in iterator)
