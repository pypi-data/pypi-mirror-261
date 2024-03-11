html_content = """
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
</head>
<body class="bg-gray-100">
    <header class="bg-blue-500 py-4">
        <div class="container mx-auto flex items-center justify-between px-4">
            <a href="#" class="text-white font-bold text-xl">Djamal</a>
            <nav>
                <!-- Add navigation links here if needed -->
            </nav>
        </div>
    </header>

    <div class="container mx-auto py-8">
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
    </div>

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
