var formData = {};

document.getElementById('btnPrevisao').addEventListener('click', function () {
    // Obter os dados do formulário
    formData = {
        campo1: parseFloat(document.getElementById('campo1').value),
        campo2: parseFloat(document.getElementById('campo2').value),
        campo3: parseFloat(document.getElementById('campo3').value),
        campo4: parseFloat(document.getElementById('campo4').value),
        campo5: parseFloat(document.getElementById('campo5').value)
    };

    // Enviar dados para o servidor usando fetch
    fetch('/realizar_predicao/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData),
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Erro na solicitação.');
        }
        return response.json();
    })
     .then(data => {
         // Atualizar o campo de resultado com a previsão
         document.getElementById('resultado').value = data.predicao; 
     })

     .catch(error => {
        console.error('Erro:', error);
        // Trate o erro conforme necessário
    });
});
 

    // Rafael Leal - Adicionar porcentagem no resultado
    //.then(data => {
        //console.log(data); // Verificar o conteúdo dos dados retornados no console
        // Atualizar o campo de resultado com a previsão e a probabilidade
        //document.getElementById('resultado').value = `Previsão: ${data.predicao}, Probabilidade: ${parseFloat(data.probabilidade).toFixed(2)}%`;

    //})
    
    
  