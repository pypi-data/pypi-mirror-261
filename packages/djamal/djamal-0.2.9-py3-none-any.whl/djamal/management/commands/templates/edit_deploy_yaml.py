html_content="""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Edit Deploy YAML File</title>
    <link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet">
    <style>
        /* Add custom styles here */
    </style>
    <script src="https://cdn.jsdelivr.net/npm/alpinejs@2.8.2/dist/alpine.min.js" defer></script>
</head>
<body class="bg-gray-100 flex flex-col h-screen">
    <!-- Header -->
    <header class="bg-blue-500 py-4">
        <div class="container mx-auto flex items-center justify-between px-4">
            <a href="{% url 'djamal_admin' %}" class="text-white font-bold text-xl">Djamal Admin</a>
            <nav>
                <!-- Add navigation links here if needed -->
            </nav>
        </div>
    </header>

    <!-- Main Content -->
    <div class="flex-1 flex">
        <!-- Sidebar -->
        <nav class="bg-gray-200 max-w-max-content p-4">
            <ul>
                <li class="mb-2"><a href="{% url 'edit_deploy_yaml' %}" onclick="executeCommand('edit_deployment_file')" class="text-blue-500 hover:underline">Edit Deployment File</a></li>
                <li class="mb-2"><a href="#" onclick="executeCommand('deploy')" class="text-blue-500 hover:underline">Deploy to Server/s</a></li>
                <li x-data="{ open: false }" class="mb-2">
                    <a href="#" @click="open = !open" class="text-blue-500 hover:underline flex items-center justify-between">
                        Advanced Options
                        <svg x-show="open" class="w-4 h-4 ml-1" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 15l7-7 7 7"></path></svg>
                        <svg x-show="!open" class="w-4 h-4 ml-1" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path></svg>
                    </a>
                    <ul x-show="open" class="ml-4">
                        <!-- Advanced options list -->
                        <li><a href="#" onclick="executeCommand('add_alias')" class="text-blue-500 hover:underline">Add Alias</a></li>
                        <li><a href="#" onclick="executeCommand('help_text')" class="text-blue-500 hover:underline">Help Text</a></li>
                        <li><a href="#" onclick="executeCommand('print_version')" class="text-blue-500 hover:underline">Print Version</a></li>
                        <li><a href="#" onclick="executeCommand('setup_djamal')" class="text-blue-500 hover:underline">Setup Djamal</a></li>
                        <li><a href="#" onclick="executeCommand('accessory')" class="text-blue-500 hover:underline">Accessory</a></li>
                        <li><a href="#" onclick="executeCommand('app')" class="text-blue-500 hover:underline">App</a></li>
                        <li><a href="#" onclick="executeCommand('audit')" class="text-blue-500 hover:underline">Audit</a></li>
                        <li><a href="#" onclick="executeCommand('build')" class="text-blue-500 hover:underline">Build</a></li>
                        <li><a href="#" onclick="executeCommand('config')" class="text-blue-500 hover:underline">Config</a></li>
                        <li><a href="#" onclick="executeCommand('details')" class="text-blue-500 hover:underline">Details</a></li>
                        <li><a href="#" onclick="executeCommand('env')" class="text-blue-500 hover:underline">Env</a></li>
                        <li><a href="#" onclick="executeCommand('envify')" class="text-blue-500 hover:underline">Envify</a></li>
                        <li><a href="#" onclick="executeCommand('healthcheck')" class="text-blue-500 hover:underline">Healthcheck</a></li>
                        <li><a href="#" onclick="executeCommand('init')" class="text-blue-500 hover:underline">Init</a></li>
                        <li><a href="#" onclick="executeCommand('lock')" class="text-blue-500 hover:underline">Lock</a></li>
                        <li><a href="#" onclick="executeCommand('prune')" class="text-blue-500 hover:underline">Prune</a></li>
                        <li><a href="#" onclick="executeCommand('redeploy')" class="text-blue-500 hover:underline">Redeploy</a></li>
                        <li><a href="#" onclick="executeCommand('registry')" class="text-blue-500 hover:underline">Registry</a></li>
                        <li><a href="#" onclick="executeCommand('remove')" class="text-blue-500 hover:underline">Remove</a></li>
                        <li><a href="#" onclick="executeCommand('rollback')" class="text-blue-500 hover:underline">Rollback</a></li>
                        <li><a href="#" onclick="executeCommand('server')" class="text-blue-500 hover:underline">Server</a></li>
                        <li><a href="#" onclick="executeCommand('setup')" class="text-blue-500 hover:underline">Setup</a></li>
                        <li><a href="#" onclick="executeCommand('traefik')" class="text-blue-500 hover:underline">Traefik</a></li>
                    </ul>
                </li>
            </ul>
        </nav>

        <!-- Form Content -->
        <main class="container mx-auto py-8 flex-1">
            <h1 class="text-2xl font-bold mb-4">Edit Deploy YAML</h1>
            <form method="post">
                {% csrf_token %}
                {% if messages %}
                    <ul class="text-red-500">
                        {% for message in messages %}
                            <li>{{ message }}</li>
                        {% endfor %}
                    </ul>
                {% endif %}
                <div class="mb-4">
                    {{ form.yaml_content.label_tag }}
                    <textarea name="yaml_content" id="yaml_content" class="w-full h-96 bg-white border border-gray-300 rounded py-2 px-4 resize-none">{{ form.yaml_content.value }}</textarea>
                </div>
                <button type="submit" class="bg-blue-500 hover:bg-blue-600 text-white font-bold py-2 px-4 rounded">
                    Save
                </button>
            </form>
        </main>
    </div>

    <!-- Footer -->
    <footer class="bg-gray-200 py-4 text-center">
        <div>
            <p><b><a href="https://appliku.com/?via=djamal">Get Your Servers here</a></b></p>
            <p class="text-gray-500 text-sm">© 2023 Djamal Admin</p>
        </div>
    </footer>

    <!-- Script for showing a success message without redirecting -->
    <script>
        // Check if the URL contains a success parameter indicating a successful form submission
        const urlParams = new URLSearchParams(window.location.search);
        if (urlParams.has('success')) {
            // Show success message
            const successMessage = document.createElement('div');
            successMessage.classList.add('bg-green-500', 'text-white', 'p-4', 'rounded', 'mb-4');
            successMessage.textContent = 'YAML content saved successfully!';
            document.body.prepend(successMessage);
            // Remove the success parameter from the URL
            window.history.replaceState({}, document.title, window.location.pathname);
        }
    </script>
</body>
</html>

"""