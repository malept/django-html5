"""
HTML5 input widgets.
TODO: Date widgets
"""
from django.forms.widgets import (
    DateInput as DjangoDateInput, DateTimeInput as DjangoDateTimeInput,
    Input, TextInput as DjangoTextInput, TimeInput as DjangoTimeInput)


class HTML5InputMixin(object):
    use_autofocus_fallback = False

    def render(self, *args, **kwargs):
        rendered_string = super(self.__class__, self).render(*args, **kwargs)
        # js only works when an id is set
        if self.use_autofocus_fallback and kwargs.has_key('attrs') and kwargs['attrs'].get("id",False) and kwargs['attrs'].has_key("autofocus"):
            rendered_string += """<script>
if (!("autofocus" in document.createElement("input"))) {
  document.getElementById("%s").focus();
}
</script>""" % kwargs['attrs']['id']
        return rendered_string


class HTML5Input(Input, HTML5InputMixin):
    pass


class TextInput(DjangoTextInput, HTML5InputMixin):
    input_type = 'text'

class EmailInput(TextInput):
    input_type = 'email'

class URLInput(TextInput):
    input_type = 'url'

class SearchInput(TextInput):
    input_type = 'search'

class ColorInput(HTML5Input):
    """
    Not supported by any browsers at this time (Jan. 2010).
    """
    input_type = 'color'

class NumberInput(HTML5Input):
    input_type = 'number'

class RangeInput(NumberInput):
    input_type = 'range'

class DateInput(DjangoDateInput, HTML5InputMixin):
    input_type = 'date'

class MonthInput(HTML5Input):
    input_type = 'month'

class WeekInput(HTML5Input):
    input_type = 'week'

class TimeInput(DjangoTimeInput, HTML5InputMixin):
    input_type = 'time'

class DateTimeInput(DjangoDateTimeInput, HTML5InputMixin):
    input_type = 'datetime'

class DateTimeLocalInput(DjangoDateTimeInput, HTML5InputMixin):
    input_type = 'datetime-local'
