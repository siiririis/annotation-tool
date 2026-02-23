function displayDocument(doc) {
    document.getElementById("document-text").textContent = doc.text;
}

async function uploadFile(file) {
    const formData = new FormData();
    formData.append("file", file);

    const response = await fetch("/upload", {
        method: "POST",
        body: formData
    });

    const data = await response.json();
    displayDocument(data);
}

document.getElementById("annotation-file").addEventListener("change", (event) => {
    const file = event.target.files[0];
    if (file) uploadFile(file);
})