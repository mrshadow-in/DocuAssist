from django import forms
from .models import DiagnosticReport


class DiagnosticReportForm(forms.ModelForm):
    class Meta:
        model = DiagnosticReport
        fields = ['report_file']  # Specify the fields you want in the form

    def __init__(self, *args, **kwargs):
        super(DiagnosticReportForm, self).__init__(*args, **kwargs)
        self.fields['report_file'].widget.attrs.update(
            {'accept': '.png, .jpg, .jpeg, .pdf'})  # Limit accepted file types
