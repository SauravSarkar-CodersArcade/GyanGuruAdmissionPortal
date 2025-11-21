// static/ajax_file_upload.js

function uploadFile(input, field) {
    const file = input.files[0];
    if (!file) return;
    const formData = new FormData();
    formData.append('file', file);
    formData.append('field', field);
    const status = document.getElementById("file_status_" + field);
    status.textContent = "Uploading...";
    status.className = "file-status text-warning small mt-1";
    fetch('/upload_temp_file', {
        method: 'POST',
        body: formData,
        credentials: "same-origin"
    })
    .then(resp => resp.json())
    .then(data => {
        if (data.filename) {
            status.textContent = "Already uploaded: " + data.filename;
            status.className = "file-status text-success small mt-1";

            // Update preview modal file name if visible
            var previewModal = document.getElementById('previewModal');
            if(previewModal && previewModal.classList.contains('show')) {
                var modalField = document.querySelector('#previewModal [id="p_' + field + '"]');
                if(modalField) {
                    modalField.textContent = data.filename;
                }
            }
        } else if (data.error) {
            status.textContent = "Error: " + data.error;
            status.className = "file-status text-danger small mt-1";
        }
    })
    .catch(err => {
        status.textContent = "Upload error!";
        status.className = "file-status text-danger small mt-1";
    });
}
