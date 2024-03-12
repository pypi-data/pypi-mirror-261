html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Admin Dashboard</title>
    <link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet">
    <script src="https://cdn.jsdelivr.net/npm/alpinejs@3.x.x/dist/cdn.min.js" defer></script>
    <script src="https://cdn.jsdelivr.net/gh/alpinejs/alpine@v2.x.x/dist/alpine.min.js" defer></script>
</head>
<body class="bg-gray-100 font-sans leading-normal tracking-normal">

    <!-- Sidebar -->
    <div class="flex h-screen">
        <aside class="bg-white shadow-md h-full w-64 px-5 py-8">
            <div class="flex flex-col justify-between h-full">
                <div>
                    <h1 class="text-2xl font-bold mb-6">Djamal Admin</h1>
                    <nav>
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
                </div>
                <div>
                    <p class="text-gray-500 text-sm">© 2023 Djamal Admin</p>
                </div>
            </div>
        </aside>

        <!-- Main Content -->
        <main class="flex-1 p-8">
            <div id="responseCard" class="bg-white p-4 shadow rounded-lg hidden">
                <h2 class="text-lg font-semibold mb-4">Response</h2>
                <div id="responseContent"></div>
            </div>
        </main>
    </div>

    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
    <script>
        function executeCommand(commandName) {
            $.ajax({
                url: `/djamal/${commandName}/`,
                type: 'GET',
                success: function(response) {
                    // Update the DOM with the response content
                    $('#responseContent').html(response); // Update response content
                    $('#responseCard').removeClass('hidden'); // Show response card
                },
                error: function(xhr, status, error) {
                    console.error('Error:', error);
                }
            });
        }
    </script>

</body>
</html>
"""