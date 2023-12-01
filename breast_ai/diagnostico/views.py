from django.shortcuts import render
from django.http import JsonResponse
import joblib
import json
from django.views.decorators.csrf import csrf_exempt

# Carregar o modelo .pkl
modelo = joblib.load('./diagnostico/modeloTreinamento.pkl')

def index(request):
    # return render(request, 'diagnostico/index.html')
    return render(request, './diagnostico/index.html')

@csrf_exempt
def realizar_predicao(request):
    try:
        # Obter os dados do formulário
        dados = json.loads(request.body)

        # Realizar a previsão usando o modelo
        predicao = modelo.predict([[dados['campo1'], dados['campo2'], dados['campo3'], dados['campo4'], dados['campo5']]])

        # Converta o resultado do modelo para string ('Maligno' ou 'Benigno')
        predicao_str = 'Benigno' if predicao[0] == 1 else 'Maligno'


        # A resposta é enviada de volta ao frontend
        return JsonResponse({'predicao': predicao_str})
    except Exception as e:
        return JsonResponse({'error': str(e)})
