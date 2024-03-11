import sys
from asgiref.sync import async_to_sync

from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.core.management import call_command
from django.contrib import messages


from djamal.management.commands.djamal import Command

from .forms import DeployForm


def djamal_admin(request):
    return render(request, "admin.html")


def call_function(request, function_name):
    # Dynamically call the function based on the function_name parameter
    if hasattr(sys.modules[__name__], function_name):
        func = getattr(sys.modules[__name__], function_name)
        output = async_to_sync(func(request))
        return JsonResponse({"output": output})
    else:
        return JsonResponse({"error": f"Function {function_name} not found."})


def execute_djamal_command(request, command_name, *args):
    command_instance = Command()
    options = request.GET.copy()
    options["command"] = command_name
    output = command_instance.handle(**options)
    return output


def add_alias(request):
    # Execute the add_alias command
    execute_djamal_command(request, "add_alias")
    return JsonResponse({"message": "Alias added successfully."})


def help_text(request):
    # Execute the help command
    output = execute_djamal_command(request, "help")
    return JsonResponse({"output": output})


def print_version(request):
    # Execute the version command
    output = execute_djamal_command(request, "version")
    return JsonResponse({"output": output})


def setup_djamal(request):
    # Execute the setup_djamal command
    execute_djamal_command(request, "setup_djamal")
    return JsonResponse({"message": "Djamal setup command executed successfully."})


def accessory(request, *args):
    # Execute the accessory command
    output = execute_djamal_command(request, "accessory", *args)
    return JsonResponse({"output": output})


def app(request, *args):
    # Execute the app command
    output = execute_djamal_command(request, "app", *args)
    return JsonResponse({"output": output})


def audit(request, *args):
    # Execute the audit command
    output = execute_djamal_command(request, "audit", *args)
    return JsonResponse({"output": output})


def build(request, *args):
    # Execute the build command
    output = execute_djamal_command(request, "build", *args)
    return JsonResponse({"output": output})


def config(request, *args):
    # Execute the config command
    output = execute_djamal_command(request, "config", *args)
    return JsonResponse({"output": output})


def deploy(request, *args):
    # Execute the deploy command
    output = execute_djamal_command(request, "deploy", *args)
    return JsonResponse({"output": output})


def details(request, *args):
    # Execute the details command
    output = execute_djamal_command(request, "details", *args)
    return JsonResponse({"output": output})


def env(request, *args):
    # Execute the env command
    output = execute_djamal_command(request, "env", *args)
    return JsonResponse({"output": output})


def envify(request, *args):
    # Execute the envify command
    output = execute_djamal_command(request, "envify", *args)
    return JsonResponse({"output": output})


def healthcheck(request, *args):
    # Execute the healthcheck command
    output = execute_djamal_command(request, "healthcheck", *args)
    return JsonResponse({"output": output})


def init(request, *args):
    # Execute the init command
    output = execute_djamal_command(request, "init", *args)
    return JsonResponse({"output": output})


def lock(request, *args):
    # Execute the lock command
    output = execute_djamal_command(request, "lock", *args)
    return JsonResponse({"output": output})


def prune(request, *args):
    # Execute the prune command
    output = execute_djamal_command(request, "prune", *args)
    return JsonResponse({"output": output})


def redeploy(request, *args):
    # Execute the redeploy command
    output = execute_djamal_command(request, "redeploy", *args)
    return JsonResponse({"output": output})


def registry(request, *args):
    # Execute the registry command
    output = execute_djamal_command(request, "registry", *args)
    return JsonResponse({"output": output})


def remove(request, *args):
    # Execute the remove command
    output = execute_djamal_command(request, "remove", *args)
    return JsonResponse({"output": output})


def rollback(request, *args):
    # Execute the rollback command
    output = execute_djamal_command(request, "rollback", *args)
    return JsonResponse({"output": output})


def server(request, *args):
    # Execute the server command
    output = execute_djamal_command(request, "server", *args)
    return JsonResponse({"output": output})


def setup(request, *args):
    # Execute the setup command
    output = execute_djamal_command(request, "setup", *args)
    return JsonResponse({"output": output})


def traefik(request, *args):
    # Execute the traefik command
    output = execute_djamal_command(request, "traefik", *args)
    return JsonResponse({"output": output})


def create_djamal_extension(request, *args):
    # Execute the create_djamal_extension command
    output = execute_djamal_command(request, "create_djamal_extension", *args)
    return JsonResponse({"output": output})


def edit_deploy_yaml(request):
    if request.method == "POST":
        form = DeployForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "File saved successfully.")
            return redirect("edit_deploy_yaml")
    else:
        form = DeployForm()
    return render(request, "edit_deploy_yaml.html", {"form": form})
