html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Admin Page</title>
    <link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet">
</head>
<body class="bg-gray-100 font-sans leading-normal tracking-normal">

    <!-- Navbar -->
    <nav class="bg-white p-4 shadow">
        <div class="container mx-auto">
            <div class="flex justify-between items-center">
                <div class="text-xl font-semibold">Djamal Admin Dashboard</div>
            </div>
        </div>
    </nav>

    <!-- Content -->
    <div class="container mx-auto mt-8">
        <div class="grid grid-cols-1 md:grid-cols-3 lg:grid-cols-4 gap-4">
            <div class="bg-white p-4 shadow rounded-lg">
                <h2 class="text-lg font-semibold mb-4">Commands</h2>
                <ul>
                    <li><a href="#" onclick="executeCommand('add_alias')" class="text-blue-500 hover:underline">Add Alias</a></li>
                    <li><a href="#" onclick="executeCommand('help_text')" class="text-blue-500 hover:underline">Help Text</a></li>
                    <li><a href="#" onclick="executeCommand('print_version')" class="text-blue-500 hover:underline">Print Version</a></li>
                    <li><a href="#" onclick="executeCommand('setup_djamal')" class="text-blue-500 hover:underline">Setup Djamal</a></li>
                    <li><a href="#" onclick="executeCommand('accessory')" class="text-blue-500 hover:underline">Accessory</a></li>
                    <li><a href="#" onclick="executeCommand('app')" class="text-blue-500 hover:underline">App</a></li>
                    <li><a href="#" onclick="executeCommand('audit')" class="text-blue-500 hover:underline">Audit</a></li>
                    <li><a href="#" onclick="executeCommand('build')" class="text-blue-500 hover:underline">Build</a></li>
                    <li><a href="#" onclick="executeCommand('config')" class="text-blue-500 hover:underline">Config</a></li>
                    <li><a href="#" onclick="executeCommand('deploy')" class="text-blue-500 hover:underline">Deploy</a></li>
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
            </div>
            <div id="responseCard" class="bg-white p-4 shadow rounded-lg hidden">
                <h2 class="text-lg font-semibold mb-4">Response</h2>
                <div id="responseContent"></div>
            </div>
        </div>
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
