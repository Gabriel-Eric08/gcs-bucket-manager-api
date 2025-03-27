function upCredentials(event) {
    event.preventDefault(); 

    let credentialsText = document.getElementById('credentials').value;
    
    let credentialsObj;
    try {
        credentialsObj = JSON.parse(credentialsText);
    } catch (error) {
        alert("Erro: JSON inválido! Verifique a formatação.");
        return;
    }

    const options = {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(credentialsObj),
    };

    fetch('http://127.0.0.1:5000/auth/uploadcredentials', options)
    .then(response => {
        if (!response.ok) {
            throw new Error(`Erro ${response.status}: ${response.statusText}`);
        }
        return response.json();
    })
    .then(update => {
        console.log("Resposta do servidor:", update);
        alert("Credenciais enviadas com sucesso!");
    })
    .catch(error => {
        console.error("Erro na requisição:", error);
        alert("Erro ao enviar credenciais. Verifique o console para mais detalhes.");
    });
}
