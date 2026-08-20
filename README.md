# Pipeline de Prevenção a Fraudes (Liveness Detection) 🛡️

## 📌 O Problema de Negócio
Instituições financeiras lidam diariamente com tentativas de fraudes de identidade, onde criminosos utilizam fotos impressas ou telas para burlar sistemas de biometria (*Spoofing*). O objetivo deste projeto é mitigar esse risco de forma automatizada e escalável.

## 💡 A Solução e Arquitetura
Desenvolvimento de um pipeline *End-to-End* que simula o fluxo de aprovação de um banco. A arquitetura foi estruturada para garantir velocidade de decisão e conformidade regulatória (trilha de auditoria).
* O modelo de IA (MobileNetV2 com Transfer Learning) classifica a imagem.
* O Apache Airflow orquestra as tarefas de validação e regras de negócio.
* O Docker isola o ambiente garantindo estabilidade corporativa.

## 📊 Resultados Alcançados (Impacto)
*   **Acurácia de Validação:** 81% (baseline sólida para MVP).
*   Implementação de registros (logs) automatizados simulando aprovação direta ou envio para mesa de fraude, dependendo do risco avaliado.

## 🛠️ Tecnologias Utilizadas
* Python, TensorFlow/Keras, OpenCV
* Apache Airflow, Docker, WSL
* SQL

## ⚙️ Como executar este projeto
1. Clone o repositório: [git clone https://github.com/marcosjcn94-bit/liveness-detection-pipeline.git]
2. Inicialize o servidor Docker: `docker compose up -d`
3. Acesse o Airflow no navegador: `http://localhost:8080`
