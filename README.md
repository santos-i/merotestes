Programa desenvolvido para teste e controle de qualidade dos sensores meteorológicos young.

Na pasta translator encontra-se a configuração, que deve ser importada para o Translator modelo 26800, e um resumo de como os sensores devem ser conectados.
O script lê e processa o log dos sensores, gerando gráficos interativos (em html) com a biblioteca plotly, para facilitar a visualização e interpretação dos dados.

O arquivo .env contém o número de série dos sensores que estão sendo testados, sendo necessária atualização a cada rodada de teste ou quando houver substituição do equipamento.
