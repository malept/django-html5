from django.forms.fields import *


def _widget_attrs(self, widget):
    attrs = {}
    if self.required:
        attrs['required'] = 'required'
    return attrs
Field.widget_attrs = _widget_attrs


def _char_widget_attrs(self, widget):
    attrs = super(CharField, self).widget_attrs(widget)
    more_attrs = self._more_widget_attrs(widget)
    if more_attrs:
        attrs.update(more_attrs)
    return attrs
CharField._more_widget_attrs = CharField.widget_attrs
CharField.widget_attrs = _char_widget_attrs


def _set_minmax_widget_attrs(cls):
    def _minmax_widget_attrs(self, widget):
        """
        Given a Widget instance (*not* a Widget class), returns a dictionary of
        any HTML attributes that should be added to the Widget, based on this
        Field.
        """
        attrs = super(cls, self).widget_attrs(widget)
        if getattr(self, 'min_value', None) is not None:
            attrs['min'] = self.min_value
        if getattr(self, 'max_value', None) is not None:
            attrs['max'] = self.max_value
        return attrs
    cls.widget_attrs = _minmax_widget_attrs
[_set_minmax_widget_attrs(cls) for cls in [DecimalField, IntegerField]]
