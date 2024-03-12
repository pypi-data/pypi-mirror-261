

class HtmxViewMixin:
    """ Mixin used to check if a request is htmx."""
    def is_htmx(self):
        """Check if a request is htmx; determined by inclusion of Hx-Request header.

        Returns:
            True if request is htmx, otherwise False
        """
        if self.request.headers.get("Hx-Request", None):
            return True
        return False
