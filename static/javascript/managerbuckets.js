function deletBucket(lineId) {
    let line = document.getElementById(lineId);
    let bucket_name = line.children[1].textContent;

    const options = {
        method: 'DELETE',
    };

    fetch('http://127.0.0.1:5000/buckets/' + bucket_name, options)
    .then(response => {
        if (!response.ok) {
            throw new Error(`Erro ${response.status}: ${response.statusText}`);
        }
        return response.json();
    })
    .then(update => {
        console.log("Resposta do servidor:", update);
        alert("Bucket deletado com sucesso!");
        line.remove();
    })
    .catch(error => {
        console.error("Erro na requisição:", error);
        alert("Erro ao deletar bucket. Verifique o console para mais detalhes.");
    });
}

function createBucket() {
    let bucket_name = document.getElementById('bucket_name').value.trim();

    if (!bucket_name) {
        alert("Por favor, insira um nome para o bucket.");
        return;
    }

    const options = {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ "bucket_name": bucket_name })
    };

    fetch('http://127.0.0.1:5000/buckets/', options)
    .then(response => {
        if (!response.ok) {
            throw new Error(`Erro ${response.status}: ${response.statusText}`);
        }
        return response.json();
    })
    .then(update => {
        console.log("Resposta do servidor:", update);
        alert("Bucket criado com sucesso!");

    })
    .catch(error => {
        console.error("Erro na requisição:", error);
        alert("Erro ao criar bucket. Verifique o console para mais detalhes.");
    });
}
