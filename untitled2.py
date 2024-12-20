# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1yOh6M2iWBARlD4SDW73fC5Mo7pGihw0K
"""

!pip install dash
import numpy as np
import plotly.graph_objects as go
from scipy.stats import beta, binom,gamma, norm, invgamma
# Funções de probabilidade
def plot_beta_distribution(a, b):
    # Gera valores de theta no intervalo (0,1), evitando extremos
    theta = np.linspace(0, 1, 1000)

    # Se for a Beta(1,1), a densidade é sempre 1
    if a == 1 and b == 1:
        beta_pdf = np.ones_like(theta)
    else:
        from scipy.stats import beta
        beta_pdf = beta.pdf(theta, a, b)

    # Cria o gráfico usando Plotly
    fig = go.Figure()

    # Adiciona a curva da densidade
    fig.add_trace(go.Scatter(
        x=theta,
        y=beta_pdf,
        mode='lines',
        name=f'Beta({a}, {b})',
        line=dict(color='royalblue', width=2)
    ))

    # Configurações do gráfico
    fig.update_layout(
        title=f'Distribuição Beta({a}, {b})',
        xaxis_title='p (Probabilidade de Sucesso)',
        yaxis_title='Densidade',
        template='plotly_white'
    )
    return fig


def plot_gamma_distribution(a, b):
    # Calcula a moda da distribuição Gamma (somente para a > 1)
    if a > 1:
        mode = (a - 1) / b
    else:
        mode = 0  # Não há moda definida para a <= 1
    # Ajusta o intervalo de x ao redor da moda, aumentando o intervalo
    x_min = max(0, mode - 3*np.sqrt(a/b**2))  # Aumenta o limite mínimo
    x_max = mode + 3*np.sqrt(a/b**2)          # Aumenta o limite máximo

    # Gera valores de x no intervalo ajustado
    x = np.linspace(x_min, x_max, 100000)

    # Calcula a densidade da Gamma(a, scale=1/b)
    gamma_pdf = gamma.pdf(x, a, scale=1/b)

    # Cria o gráfico usando Plotly
    fig = go.Figure()

    # Adiciona a curva da densidade
    fig.add_trace(go.Scatter(
        x=x,
        y=gamma_pdf,
        mode='lines',
        name=f'Gamma({a}, {b})',
        line=dict(color='royalblue', width=2)
    ))

    # Personalizações do layout
    fig.update_layout(
        title=f'Distribuição Gama({a}, {b})',
        xaxis_title='x',
        yaxis_title='Densidade',
        template='plotly_white',
        showlegend=True
    )

    # Exibe a figura
    return fig

def plot_normal_distribution(mu, sigma2):
    # Desvio padrão é a raiz quadrada da variância
    sigma = np.sqrt(sigma2)

    # Gera valores de x ao redor da média (mu), cobrindo a maior parte da densidade
    x = np.linspace(mu - 4*sigma, mu + 4*sigma, 1000)

    # Calcula a função densidade de probabilidade (PDF) da Normal
    normal_pdf = norm.pdf(x, mu, sigma)

    # Cria o gráfico usando Plotly
    fig = go.Figure()

    # Adiciona a curva da densidade
    fig.add_trace(go.Scatter(
        x=x,
        y=normal_pdf,
        mode='lines',
        name=f'Normal({mu}, {sigma2})',
        line=dict(color='royalblue', width=2)
    ))

    # Configurações do gráfico
    fig.update_layout(
        title=f'Distribuição Normal({mu}, {sigma2})',
        xaxis_title='x',
        yaxis_title='Densidade',
        template='plotly_white'
    )

    return fig


def verossimilhanca_binomial_aproximada(x,m,n):
  figura=plot_beta_distribution(n*x+1,n*(m-x)+1)
  figura.data[0].line.color = 'red'
  figura.update_layout(
      title="Verossimilhança aproximada da Binomial",
      yaxis_title="Verossimilhança"
  )
  return figura

def verossimilhanca_poisson_aproximada(x,n):
  figura=plot_gamma_distribution(n*x+1,n)
  figura.data[0].line.color = 'red'
  figura.update_layout(
      title="Verossimilhança aproximada da Poisson",
      yaxis_title="Verossimilhança"
  )
  return figura

def verossimilhanca_binomial_negativa_aproximada(x,r,n):
  figura=plot_beta_distribution(n*r+1,n*(x-r)+1)
  figura.data[0].line.color = 'red'
  figura.update_layout(
      title="Verossimilhança aproximada da Binomial negativa",
      yaxis_title="Verossimilhança"
  )
  return figura
def verossimilhanca_gama_aproximada(x,a,n):
  figura=plot_gamma_distribution(n*a+1,n*x)
  figura.data[0].line.color = 'red'
  figura.update_layout(
      title="Verossimilhança aproximada da Gama",
      yaxis_title="Verossimilhança"
  )
  return figura
def verossimilhanca_exponencial_aproximada(x,n):
  figura=plot_gamma_distribution(n+1,n*x)
  figura.data[0].line.color = 'red'
  figura.update_layout(
      title="Verossimilhança aproximada da Exponencial",
      yaxis_title="Verossimilhança"
  )
  return figura

def verossimilhanca_normal_aproximada(x,sigma2,n):
  figura=plot_normal_distribution(x,sigma2/n)
  figura.data[0].line.color = 'red'
  figura.update_layout(
      title="Verossimilhança aproximada da Normal",
      yaxis_title="Verossimilhança"
  )
  return figura

def verossimilhanca_bernoulli_aproximada(x,n):
  figura=plot_beta_distribution(n*x+1,n*(1-x)+1)
  figura.data[0].line.color = 'red'
  figura.update_layout(
      title="Verossimilhança aproximada da Bernoulli",
      yaxis_title="Verossimilhança"
  )
  return figura
def verossimilhanca_geometrica_aproximada(x,n):
  figura=plot_beta_distribution(n+1,n*(x-1)+1)
  figura.data[0].line.color = 'red'
  figura.update_layout(
      title="Verossimilhança aproximada da Geométrica",
      yaxis_title="Verossimilhança"
  )
  return figura

def beta_pdf(a,b):
    theta = np.linspace(0, 1, 1000)
    if a == 1 and b == 1:
        beta_pdf = np.ones_like(theta)
    else:
        from scipy.stats import beta
        beta_pdf = beta.pdf(theta, a, b)
    return beta_pdf

def beta_binomial(a, b,x,m,n):
    # Cria o gráfico usando Plotly
    fig = go.Figure()
    eixo_x=np.linspace(0,1,1000)
    y_priori=beta_pdf(a,b)
    y_verossimilhanca=beta_pdf(n*x+1,n*(m-x)+1)
    y_posteriori=beta_pdf(n*x+a,b+n*(m-x))
    # Adiciona a curva da densidade da priori
    fig.add_trace(go.Scatter(
        x=eixo_x,
        y=y_priori,
        mode='lines',
        name=f'Beta({a}, {b})',
        line=dict(color='royalblue', width=2)
    ))
    fig.add_trace(go.Scatter(
        x=eixo_x,
        y=y_verossimilhanca,
        mode='lines',
        name=f'Beta({n*x+1}, {n*(m-x)+1})',
        line=dict(color='red', width=2)
    ))
    fig.add_trace(go.Scatter(
        x=eixo_x,
        y=y_posteriori,
        mode='lines',
        name=f'Beta({n*x+a}, {b+n*(m-x)})',
        line=dict(color='green', width=2)
    ))
    # Configurações do gráfico
    fig.update_layout(
        title=f'Distribuição Beta-Binomial',
        xaxis_title='p (Probabilidade de Sucesso)',
        yaxis_title='Densidade',
        template='plotly_white'
    )
    return fig

def beta_bernoulli(a,b,x,n):
    # Cria o gráfico usando Plotly
    fig = go.Figure()
    eixo_x=np.linspace(0,1,1000)
    y_priori=beta_pdf(a,b)
    y_verossimilhanca=beta_pdf(round(n*x+1,2),round(n*(1-x)+1,2))
    y_posteriori=beta_pdf(a+n*x,b+n*(1-x))
    # Adiciona a curva da densidade da priori
    fig.add_trace(go.Scatter(
        x=eixo_x,
        y=y_priori,
        mode='lines',
        name=f'Beta({a}, {b})',
        line=dict(color='royalblue', width=2)
    ))
    fig.add_trace(go.Scatter(
        x=eixo_x,
        y=y_verossimilhanca,
        mode='lines',
        name=f'Beta({round(n*x+1,2)}, {round(n*(1-x)+1,2)})',
        line=dict(color='red', width=2)
    ))
    fig.add_trace(go.Scatter(
        x=eixo_x,
        y=y_posteriori,
        mode='lines',
        name=f'Beta({a+n*x}, {b+n*(1-x)})',
        line=dict(color='green', width=2)
    ))
    # Configurações do gráfico
    fig.update_layout(
        title=f'Distribuição Beta-Bernoulli',
        xaxis_title='p (Probabilidade de Sucesso)',
        yaxis_title='Densidade',
        template='plotly_white'
    )
    return fig

def beta_geometrica(a,b,x,n):
    # Cria o gráfico usando Plotly
    fig = go.Figure()
    eixo_x=np.linspace(0,1,1000)
    y_priori=beta_pdf(a,b)
    y_verossimilhanca=beta_pdf(n+1,n*(x-1)+1)
    y_posteriori=beta_pdf(a+n,b+n*(x-1))
    # Adiciona a curva da densidade da priori
    fig.add_trace(go.Scatter(
        x=eixo_x,
        y=y_priori,
        mode='lines',
        name=f'Beta({a}, {b})',
        line=dict(color='royalblue', width=2)
    ))
    fig.add_trace(go.Scatter(
        x=eixo_x,
        y=y_verossimilhanca,
        mode='lines',
        name=f'Beta({n+1}, {n*(x-1)+1})',
        line=dict(color='red', width=2)
    ))
    fig.add_trace(go.Scatter(
        x=eixo_x,
        y=y_posteriori,
        mode='lines',
        name=f'Beta({a+n}, {b+n*(x-1)})',
        line=dict(color='green', width=2)
    ))
    # Configurações do gráfico
    fig.update_layout(
        title=f'Distribuição Beta-Geométrica',
        xaxis_title='p (Probabilidade de Sucesso)',
        yaxis_title='Densidade',
        template='plotly_white'
    )
    return fig

def beta_binomial_negativa(a,b,x,r,n):
    # Cria o gráfico usando Plotly
    fig = go.Figure()
    eixo_x=np.linspace(0,1,1000)
    y_priori=beta_pdf(a,b)
    y_verossimilhanca=beta_pdf(n*r+1,n*(x-r)+1)
    y_posteriori=beta_pdf(a+n*r,b+n*(x-r))
    # Adiciona a curva da densidade da priori
    fig.add_trace(go.Scatter(
        x=eixo_x,
        y=y_priori,
        mode='lines',
        name=f'Beta({a}, {b})',
        line=dict(color='royalblue', width=2)
    ))
    fig.add_trace(go.Scatter(
        x=eixo_x,
        y=y_verossimilhanca,
        mode='lines',
        name=f'Beta({n*r+1}, {n*(x-r)+1})',
        line=dict(color='red', width=2)
    ))
    fig.add_trace(go.Scatter(
        x=eixo_x,
        y=y_posteriori,
        mode='lines',
        name=f'Beta({a+n*r}, {b+n*(x-r)})',
        line=dict(color='green', width=2)
    ))
    # Configurações do gráfico
    fig.update_layout(
        title=f'Distribuição Beta-Binomial negativa',
        xaxis_title='p (Probabilidade de Sucesso)',
        yaxis_title='Densidade',
        template='plotly_white'
    )
    return fig

def gama_pdf(a, b):
    if a > 1:
        mode = (a - 1) / b
    else:
        mode = 0
    x_min = max(0, mode - 3*np.sqrt(a/b**2))
    x_max = mode + 3*np.sqrt(a/b**2)
    return x_min,x_max

def gama_exponencial(a,b,x,n):
  x_min_priori,x_max_priori=gama_pdf(a,b)
  x_min_verossimilhanca,x_max_verossimilhanca=gama_pdf(n+1,n*x)
  x_min_posteriori,x_max_posteriori=gama_pdf(a+n,b+n*x)
  x_min=min(x_min_priori,x_min_verossimilhanca,x_min_posteriori)
  x_max=max(x_max_priori,x_max_verossimilhanca,x_max_posteriori)
  eixo_x=np.linspace(x_min,x_max,1000)
  y_priori=gamma.pdf(eixo_x,a,scale=1/b)
  y_verossimilhanca=gamma.pdf(eixo_x,n+1,scale=1/(n*x))
  y_posteriori=gamma.pdf(eixo_x,a+n,scale=1/(b+n*x))
  figura=go.Figure()
  figura.add_trace(go.Scatter(
        x=eixo_x,
        y=y_priori,
        mode='lines',
        name=f'Gamma({a}, {b})',
        line=dict(color='royalblue', width=2)
    ))
  figura.add_trace(go.Scatter(
        x=eixo_x,
        y=y_verossimilhanca,
        mode='lines',
        name=f'Gamma({n+1}, {n*x})',
        line=dict(color='red', width=2)
    ))
  figura.add_trace(go.Scatter(
        x=eixo_x,
        y=y_posteriori,
        mode='lines',
        name=f'Gamma({a+n}, {b+n*x})',
        line=dict(color='green', width=2)
    ))
  figura.update_layout(
      title=f'Distribuição Gama-Exponencial',
      xaxis_title='x',
      yaxis_title='Densidade',
      template='plotly_white',
      showlegend=True
    )
  return figura

def gama_poisson(a,b,x,n):
  x_min_priori,x_max_priori=gama_pdf(a,b)
  x_min_verossimilhanca,x_max_verossimilhanca=gama_pdf(n*x+1,n)
  x_min_posteriori,x_max_posteriori=gama_pdf(n*x+a,b+n)
  x_min=min(x_min_priori,x_min_verossimilhanca,x_min_posteriori)
  x_max=max(x_max_priori,x_max_verossimilhanca,x_max_posteriori)
  eixo_x=np.linspace(x_min,x_max,1000)
  y_priori=gamma.pdf(eixo_x,a,scale=1/b)
  y_verossimilhanca=gamma.pdf(eixo_x,n*x+1,scale=1/(n))
  y_posteriori=gamma.pdf(eixo_x,n*x+a,scale=1/(b+n))
  figura=go.Figure()
  figura.add_trace(go.Scatter(
        x=eixo_x,
        y=y_priori,
        mode='lines',
        name=f'Gamma({a}, {b})',
        line=dict(color='royalblue', width=2)
    ))
  figura.add_trace(go.Scatter(
        x=eixo_x,
        y=y_verossimilhanca,
        mode='lines',
        name=f'Gamma({n*x+1}, {n})',
        line=dict(color='red', width=2)
    ))
  figura.add_trace(go.Scatter(
        x=eixo_x,
        y=y_posteriori,
        mode='lines',
        name=f'Gamma({n*x+a}, {b+n})',
        line=dict(color='green', width=2)
    ))
  figura.update_layout(
      title=f'Distribuição Gama-Poisson',
      xaxis_title='x',
      yaxis_title='Densidade',
      template='plotly_white',
      showlegend=True
    )
  return figura

def gama_gama(a,b,x,conhecido,n):
  x_min_priori,x_max_priori=gama_pdf(a,b)
  x_min_verossimilhanca,x_max_verossimilhanca=gama_pdf(n*conhecido+1,n*x)
  x_min_posteriori,x_max_posteriori=gama_pdf(a+n*conhecido,b+n*x)
  x_min=min(x_min_priori,x_min_verossimilhanca,x_min_posteriori)
  x_max=max(x_max_priori,x_max_verossimilhanca,x_max_posteriori)
  eixo_x=np.linspace(x_min,x_max,1000)
  y_priori=gamma.pdf(eixo_x,a,scale=1/b)
  y_verossimilhanca=gamma.pdf(eixo_x,n*conhecido+1,scale=1/(n*x))
  y_posteriori=gamma.pdf(eixo_x,a+n*conhecido,scale=1/(b+n*x))
  figura=go.Figure()
  figura.add_trace(go.Scatter(
        x=eixo_x,
        y=y_priori,
        mode='lines',
        name=f'Gamma({a}, {b})',
        line=dict(color='royalblue', width=2)
    ))
  figura.add_trace(go.Scatter(
        x=eixo_x,
        y=y_verossimilhanca,
        mode='lines',
        name=f'Gamma({n*conhecido+1}, {n*x})',
        line=dict(color='red', width=2)
    ))
  figura.add_trace(go.Scatter(
        x=eixo_x,
        y=y_posteriori,
        mode='lines',
        name=f'Gamma({a+n*conhecido}, {b+n*x})',
        line=dict(color='green', width=2)
    ))
    # Personalizações do layout
  figura.update_layout(
      title=f'Distribuição Gama-Gama',
      xaxis_title='x',
      yaxis_title='Densidade',
      template='plotly_white',
      showlegend=True
    )

    # Exibe a figura
  return figura

def normal_pdf(mu,sigma2):
    sigma = np.sqrt(sigma2)
    return mu - 4*sigma,  mu + 4*sigma
def normal_normal(mu,sigma2,x,conhecido,n):
  x_min_priori,x_max_priori=normal_pdf(mu,sigma2)
  x_min_verossimilhanca,x_max_verossimilhanca=normal_pdf(x,conhecido/n)
  x_min_posteriori,x_max_posteriori=normal_pdf((n*sigma2*x+conhecido*mu)/(n*sigma2+conhecido),sigma2*conhecido/(n*sigma2+conhecido))
  x_min=min(x_min_priori,x_min_verossimilhanca,x_min_posteriori)
  x_max=max(x_max_priori,x_max_verossimilhanca,x_max_posteriori)
  eixo_x=np.linspace(x_min,x_max,1000)
  y_priori=norm.pdf(eixo_x,mu,np.sqrt(sigma2))
  y_verossimilhanca=norm.pdf(eixo_x,x,np.sqrt(conhecido/n))
  y_posteriori=norm.pdf(eixo_x,(n*sigma2*x+conhecido*mu)/(n*sigma2+conhecido),np.sqrt(sigma2*conhecido/(n*sigma2+conhecido)))
  figura = go.Figure()

  figura.add_trace(go.Scatter(
        x=eixo_x,
        y=y_priori,
        mode='lines',
        name=f'Normal({mu}, {sigma2})',
        line=dict(color='royalblue', width=2)
  ))
  figura.add_trace(go.Scatter(
        x=eixo_x,
        y=y_verossimilhanca,
        mode='lines',
        name=f'Normal({x}, {conhecido/n})',
        line=dict(color='red', width=2)
  ))
  figura.add_trace(go.Scatter(
        x=eixo_x,
        y=y_posteriori,
        mode='lines',
        name=f'Normal({round((n*sigma2*x+conhecido*mu)/(n*sigma2+conhecido),2)}, {round(sigma2*conhecido/(n*sigma2+conhecido),2)})',
        line=dict(color='green', width=2)
  ))
  figura.update_layout(
        title=f'Distribuição Normal-Normal',
        xaxis_title='x',
        yaxis_title='Densidade',
        template='plotly_white'
  )

  return figura

def posteriori_beta(a,b):
  figura=plot_beta_distribution(a,b)
  figura.data[0].line.color = 'green'
  return figura

def posteriori_gama(a,b):
  figura=plot_gamma_distribution(a,b)
  figura.data[0].line.color = 'green'
  return figura

def posteriori_normal(a,b):
  figura=plot_normal_distribution(a,b)
  figura.data[0].line.color = 'green'
  return figura

from dash import Dash, html, dcc, Input, Output

app = Dash(__name__)

lista_verossimilhancas=list(["Bernoulli","Binomial","Geométrica","Binomial negativa","Poisson","Exponencial","Gamma","Normal"])
lista_prioris=list(["Beta","Gamma","Normal"])

app.layout = html.Div(children=[
    html.H1(children='Trabalho de Bayesiana - Grupo PET Estatística'),
    html.H4('Selecione a distribuição da verossimilhança'),
    dcc.Dropdown(lista_verossimilhancas,value="Bernoulli",id="verossimilhancas"),
    html.H4('Selecione a distribuição da priori'),
    dcc.Dropdown(value="Beta",id="prioris"),
    html.H4('Digite os parâmetros da priori'),

    # Campo para digitar o primeiro parâmetro da priori
    html.Label(id="texto_priori_1"),
    dcc.Input(id='input-a', type='number',value=2),

    # Campo para digitar o segundo parâmetro da priori
    html.Label(id="texto_priori_2"),
    dcc.Input(id='input-b', type='number',min=0.001,value=4),

    html.Br(),

    dcc.Graph(figure=plot_beta_distribution(2,4),
        id='densidade_priori',
    ),
    html.H4('Digite os parâmetros da verossimilhança'),

    # Campo para digitar o primeiro parâmetro da verossimilhança
    html.Label(id="texto_verossimilhanca_1"),
    dcc.Input(id='input-m', type='number',min=1,step=1,value=5),
    dcc.Input(id="input-var",type="number",min=0.01,value=1),

    # Campo para digitar os valores observados
    html.Label("Digite a média amostral:"),
    dcc.Input(id='input-x', type='number',value=1),
    dcc.Input(id="input-x-bernoulli",type="number",step=0.01,min=0,max=1,value=0.7),


    # Campo para digitar o tamanho amostral
    html.Label(children="Digite o tamanho amostral:",id='texto_posteriori_2'),
    dcc.Input(id='input-tamanho', type='number',min=1,step=1,placeholder="Olá",value=3),

    # Campo para digitar o parâmetro conhecido
    html.Label(id="texto_param_conhecido"),
    dcc.Input(id='input-conhecido', type='number',value=1),


    # Gráfico da verossimilhança
    html.Br(),
    html.Div(
        dcc.Graph(figure=verossimilhanca_bernoulli_aproximada(0.7,3),
        id='densidade_verossimilhanca',),
        id='aparencia_verossimilhanca'),
    # Gráfico da posteriori
    html.Br(),
    dcc.Graph(figure=plot_beta_distribution(4.1,4.9),id="densidade_posteriori"),

    # Gráfico final
    dcc.Graph(figure=beta_bernoulli(2,4,0.7,3),id="grafico_conjunto")
])

# Atualiza as opções de seleção de priori
@app.callback(
    Output("prioris","options"),
    Input("verossimilhancas","value")
)
def update_dropdown(verossimilhancas):
    if verossimilhancas=="Bernoulli" or verossimilhancas=="Binomial" or verossimilhancas=="Geométrica" or verossimilhancas=="Binomial negativa":
        return list(["Beta"])
    elif verossimilhancas=="Gamma" or verossimilhancas=="Poisson" or verossimilhancas=="Exponencial":
        return list(["Gamma"])
    else:
        return list(["Normal"])

# Atualiza o texto do campo de digitação do primeiro parâmetro da priori
@app.callback(
    [Output("texto_priori_1","children"),
     Output("input-a","min")],
    Input("prioris","value")
)
def update_dropdown(prioris):
    if prioris=="Beta" or prioris=="Gamma":
        return "Digite o valor de a:",0.001
    else:
        return "Digite a média da priori:",None

# Atualiza o texto do campo de digitação do segundo parâmetro da priori
@app.callback(
    [Output("texto_priori_2","children"),
     Output("input-b","style")],
    Input("prioris","value")
)
def update_dropdown(prioris):
    if prioris=="Beta" or prioris=="Gamma":
        return "Digite o valor de b:",{}
    else:
        return "Digite a variância da priori:",{}

# Atualiza o gráfico da priori
@app.callback(
    Output('densidade_priori', 'figure'),
    [Input('input-a', 'value'),
     Input('input-b', 'value'),
     Input("prioris","value")]
)
def update_output(a, b,prioris):
  if(prioris=="Gamma"):
    return plot_gamma_distribution(a,b)
  elif (prioris=="Beta"):
    return plot_beta_distribution(a,b)
  else:
    return plot_normal_distribution(a,b)

# Atualiza o texto do campo de digitação do primeiro parâmetro da verossimilhança
@app.callback(
    [Output("texto_verossimilhanca_1","children"),
     Output("input-m","style"),
     Output("input-var","style")],
    Input("verossimilhancas","value")
)
def update_dropdown(verossimilhancas):
    if verossimilhancas=="Binomial":
        return "Digite o valor de m:",{},{"display":"none"}
    elif verossimilhancas=="Normal":
        return "",{"display":"none"},{"display":"none"}
    else:
      return "",{"display":"none"},{"display":"none"}

# Atualiza o texto do campo de digitação dos valores observados
@app.callback(
    [Output("input-x","min"),
     Output("input-x","style"),
     Output("input-x","max")],
    [Input("verossimilhancas","value"),
     Input("input-conhecido","value"),
     Input("input-m","value")]
)
def update_dropdown(verossimilhancas,conhecido,m):
    if verossimilhancas=="Bernoulli":
        return None,{"display":"none"},None
    elif verossimilhancas=="Binomial":
        return 0,{},m
    elif verossimilhancas=="Geométrica":
        return 1,{},None
    elif verossimilhancas=="Binomial negativa":
        return conhecido,{},None
    elif verossimilhancas=="Poisson":
        return 0,{},None
    elif verossimilhancas=="Exponencial":
        return 0,{},None
    elif verossimilhancas=="Gamma":
        return 0,{},None
    else:
        return None,{},None

@app.callback(
    Output("input-x-bernoulli","style"),
    Input("verossimilhancas","value")
)
def update_dropdown(verossimilhancas):
    if verossimilhancas=="Bernoulli":
        return {}
    else:
        return {"display":"none"}

# Atualiza o texto do campo de digitação do parâmetro conhecido
@app.callback(
    [Output("texto_param_conhecido","children"),
     Output("input-conhecido","style")],
    Input("verossimilhancas","value")
)
def update_dropdown(verossimilhancas):
    if verossimilhancas=="Normal":
        return "Digite a variância populacional:",{}
    elif verossimilhancas=="Gamma":
        return "Digite o valor de a conhecido:",{}
    elif verossimilhancas=="Binomial negativa":
        return "Digite o valor de r:",{}
    else:
        return "",{"display":"none"}

# Atualiza o gráfico da verossimilhança
@app.callback(
    [Output('densidade_verossimilhanca', 'figure'),
     Output('aparencia_verossimilhanca', 'style')],
    [Input('input-m', 'value'),
     Input("input-var","value"),
     Input('input-x', 'value'),
     Input('input-x-bernoulli','value'),
     Input('input-tamanho','value'),
     Input('input-conhecido','value'),
     Input('verossimilhancas','value')]
)
def update_output(m,var, x,x_bernoulli, n,conhecido,verossimilhancas):
    if verossimilhancas=="Geométrica":
      return verossimilhanca_geometrica_aproximada(x,n),{'display':'block'}
    elif verossimilhancas=="Bernoulli":
      return verossimilhanca_bernoulli_aproximada(x_bernoulli,n),{'display':'block'}
    elif verossimilhancas=="Normal":
      return verossimilhanca_normal_aproximada(x,conhecido,n),{'display':'block'}
    elif verossimilhancas=="Exponencial":
      return verossimilhanca_exponencial_aproximada(x,n),{'display':'block'}
    elif verossimilhancas=="Binomial":
      return verossimilhanca_binomial_aproximada(x,m,n),{'display':'block'}
    elif verossimilhancas=="Poisson":
      return verossimilhanca_poisson_aproximada(x,n),{'display':'block'}
    elif verossimilhancas=="Binomial negativa":
      return verossimilhanca_binomial_negativa_aproximada(x,conhecido,n),{'display':'block'}
    elif verossimilhancas=="Gamma":
      return verossimilhanca_gama_aproximada(x,conhecido,n),{'display':'block'}
    else:
      return go.Figure(),{'display':'none'}

# Atualiza o gráfico da posteriori
@app.callback(
    Output('densidade_posteriori', 'figure'),
    [Input('input-a', 'value'),
     Input('input-b', 'value'),
     Input('input-m', 'value'),
     Input('input-x', 'value'),
     Input('input-x-bernoulli','value'),
     Input('input-tamanho', 'value'),
     Input('input-conhecido', 'value'),
     Input("prioris","value"),
     Input("verossimilhancas","value")]
)
def update_output(a,b,m,x,x_bernoulli,n,conhecido,prioris,verossimilhancas):
  if verossimilhancas=="Binomial":
    return posteriori_beta(n*x+a,b+n*(m-x))
  elif verossimilhancas=="Bernoulli":
    return posteriori_beta(a+n*x_bernoulli,b+n*(1-x_bernoulli))
  elif verossimilhancas=="Poisson":
    return posteriori_gama(n*x+a,b+n)
  elif verossimilhancas=="Exponencial":
    return posteriori_gama(a+n,b+n*x)
  elif verossimilhancas=="Gamma":
    return posteriori_gama(a+n*conhecido,b+n*x)
  elif verossimilhancas=="Geométrica":
    return posteriori_beta(a+n,b+n*(x-1))
  elif verossimilhancas=="Binomial negativa":
    return posteriori_beta(a+n*conhecido,b+n*(x-conhecido))
  else:
    return posteriori_normal(round((n*b*x+a*conhecido)/(n*b+conhecido),2),round(conhecido*b/(n*b+conhecido),2))

# Atualiza o gráfico final
@app.callback(
    Output('grafico_conjunto', 'figure'),
    [Input('input-a', 'value'),
     Input('input-b', 'value'),
     Input('input-m', 'value'),
     Input('input-x', 'value'),
     Input('input-x-bernoulli','value'),
     Input('input-tamanho', 'value'),
     Input('input-conhecido', 'value'),
     Input("prioris","value"),
     Input("verossimilhancas","value")]
)
def update_output(a,b,m,x,x_bernoulli,n,conhecido,prioris,verossimilhancas):
  if verossimilhancas=="Bernoulli":
    return beta_bernoulli(a,b,x_bernoulli,n)
  elif verossimilhancas=="Binomial":
    return beta_binomial(a,b,x,m,n)
  elif verossimilhancas=="Geométrica":
    return beta_geometrica(a,b,x,n)
  elif verossimilhancas=="Binomial negativa":
    return beta_binomial_negativa(a,b,x,conhecido,n)
  elif verossimilhancas=="Exponencial":
    return gama_exponencial(a,b,x,n)
  elif verossimilhancas=="Poisson":
    return gama_poisson(a,b,x,n)
  elif verossimilhancas=="Gamma":
    return gama_gama(a,b,x,conhecido,n)
  else:
    return normal_normal(a,b,x,conhecido,n)


if __name__ == '__main__':
    app.run_server(debug=True)