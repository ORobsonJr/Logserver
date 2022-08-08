<h1>A proposta do Logserver</h1>
<p>O Logserver é um servidor que disponibiliza uma API para manuseio de usuários hospedados em um banco de dados MySql </p>
  
 <h2>Tecnologia utilizadas para a criação do servidor</h2>
 <ul>
   <li>Git</li>
   <li>Python3</li>
   <li>FastApi</li>
   <li>MySql + Querys</li>
   <li>Batch</li>

  </ul>
  
  <h2>Utilização e suas funcionalidades</h2>
<p><h3>Instalação:</h3>

<span class="emphasized">sudo python3.py main.py -i</span> 

em modo <strong>sudo</strong>, pois o mesmo irá fazer a validação de pacotes instalados no sistema e instalar dependências</p>
Isso será necessário somente pela primeira vez ou caso você esquema a chave secreta

<h3>Inicialização do servidor:</h3>
<span class="emphasized">sudo python3.py main.py runserver</span> 

<h3>Documentação do Logserver</h3>
<p>Você pode utilizar a documentação padrão do FastApi como:

 <span class="emphasized">  
   <a href="http://localhost:8000/documentation)">http://localhost:8000/documentation</a>
  </span>

  
ou pode utilizar a API própria do programa como:
<span class="emphasized">http://localhost:8000/documentation</span>
  

</p>


<h2>Requisitos</h2>
<ul>
<li>Mysql instalado e previamente configurado</li>
  <li>Uvicorn instalado</li>
<li>Python3 instalado</li>
<li>Fastapi instalado no python</li>
<li>Algum sistema linux ou VM linux</li>
<li>Conexão com internet</li>
</ul>
<p>Obs.: Muitas requisições porém ser instaladar automáticamente pelo <strong>python3 main.py -i</strong></p>
