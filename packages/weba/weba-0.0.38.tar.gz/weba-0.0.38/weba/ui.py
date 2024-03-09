from typing import TYPE_CHECKING, Any, Callable  # noqa: I001
from .component import Component, weba_html_context
from .tag.context_manager import TagContextManager

if TYPE_CHECKING:
    from bs4 import Tag


class UIFactory:
    """
    A factory class for creating UI elements dynamically based on tag names.
    """

    @staticmethod
    def _update_kwargs(kwargs: dict[str, Any]) -> None:
        """
        Update the kwargs dictionary in place to handle special cases:
        - Converts class variants to 'class'.
        - Converts 'hx_' prefixed keys to 'hx-'.
        - Converts 'for_' to 'for'.
        """
        # Handle different variations of the class attribute
        class_variants = ["_class", "class_", "klass", "cls"]

        for variant in class_variants:
            if variant in kwargs:
                kwargs["class"] = kwargs.pop(variant)
                break

        # Convert 'hx_' prefix to 'hx-' and 'for_' to 'for'
        for key in list(kwargs.keys()):
            if key.startswith("hx_"):
                kwargs[key.replace("_", "-")] = kwargs.pop(key)
            elif key == "for_":
                kwargs["for"] = kwargs.pop(key)

    def __getattr__(self, tag_name: str) -> Callable[..., TagContextManager]:
        def create_tag(*args: Any, **kwargs: Any) -> TagContextManager:
            html_context = weba_html_context.get(None)

            if html_context is None or not callable(html_context.new_tag):
                html_context = Component()
                weba_html_context.set(html_context)

            self._update_kwargs(kwargs)

            tag: Tag = html_context.new_tag(tag_name, **kwargs)  # type: ignore

            if args:
                tag.string = args[0]

            if html_context._context_stack:  # type: ignore
                current_context = html_context._context_stack[-1]  # type: ignore
                current_context.append(tag)

            if html_context._last_component is None:  # type:ignore
                html_context._last_component = tag  # type:ignore

            return TagContextManager(tag, html_context)  # type: ignore

        return create_tag


ui = UIFactory()
