import os
from django import forms
from ruamel.yaml import YAML
import yaml
from io import StringIO
import logging

logger = logging.getLogger(__name__)


class DeployForm(forms.Form):
    yaml_content = forms.CharField(widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Navigate to the parent directory of the current directory and then enter the config directory
        deploy_yaml_path = os.path.join(
            os.path.dirname(os.path.dirname(__file__)), "config", "deploy.yml"
        )
        if os.path.exists(deploy_yaml_path):
            yaml = YAML(typ="rt")
            with open(deploy_yaml_path, "r") as file:
                yaml_data = yaml.load(file)
                yaml_string = StringIO()
                yaml.dump(yaml_data, yaml_string)
                self.fields["yaml_content"].initial = yaml_string.getvalue()
        else:
            logger.warning("config/deploy.yml file not found.")

    def clean_yaml_content(self):
        yaml_content = self.cleaned_data["yaml_content"]
        yaml = YAML()
        try:
            # Validate the YAML content
            yaml.load(yaml_content)
        except yaml.YAMLError as e:
            raise forms.ValidationError(f"Invalid YAML: {e}") from e
        return yaml_content

    def save(self):
        yaml_content = self.cleaned_data["yaml_content"]
        deploy_yaml_path = os.path.join(
            os.path.dirname(os.path.dirname(__file__)), "config", "deploy.yml"
        )
        if os.path.exists(deploy_yaml_path):
            yaml = YAML()
            with open(deploy_yaml_path, "w") as file:
                yaml.dump(yaml.load(yaml_content), file)
        else:
            logger.warning("config/deploy.yml file not found.")
