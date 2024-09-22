// Function to switch the displayed version
    document.getElementById('version-selector').addEventListener('change', function() {
        // First, hide all versions
        document.querySelectorAll('.version-content').forEach(function(section) {
            section.classList.remove('active');
        });

        // Show the selected version
        const selectedVersion = this.value;
        document.getElementById('version-' + selectedVersion.charAt(1)).classList.add('active');
    });

    // Show the first version by default
    document.getElementById('version-1').classList.add('active');
