# Desafio MBA Engenharia de Software com IA - Full Cycle

Para rodar a aplicação você precisa rodar:
<pre>
docker compose up -d
</pre>

<pre>
cp .env.example .env //Altere as variáveis
</pre>

<pre>
python3 -m venv venv
</pre>

<pre>
source venv/bin/activate
</pre>

<pre>
pip install -r requirements.txt
</pre>

<pre>
python3 src/ingest.py
</pre>


<pre>
python3 src/chat.py
</pre>
