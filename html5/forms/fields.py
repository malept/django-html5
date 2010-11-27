from django.forms.fields import DecimalField, IntegerField


def _set_minmax_widget_attrs(cls):
    def _minmax_widget_attrs(self, widget):
        """
        Given a Widget instance (*not* a Widget class), returns a dictionary of
        any HTML attributes that should be added to the Widget, based on this
        Field.
        """
        attrs = super(cls, self).widget_attrs(widget)
        if self.min_value is not None:
            attrs['min'] = self.min_value
        if self.max_value is not None:
            attrs['max'] = self.max_value
        return attrs
    cls.widget_attrs = _minmax_widget_attrs
[_set_minmax_widget_attrs(cls) for cls in [DecimalField, IntegerField]]
