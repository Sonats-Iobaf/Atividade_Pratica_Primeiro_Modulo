ATP – Etapa 1
Nesta primeira etapa, vamos começar a construir o sistema da loja. Até o momento, você aprendeu a
trabalhar com variáveis em Python e com a entrada e saída de dados (utilizando as funções print e
input).
Assim, para esta etapa, faça um algoritmo que atenda às seguintes instruções:
1. Mostre ao usuário o seu nome completo, junto do nome da sua loja (não peça ao usuário o
nome dele, apenas o mostre).
a. Exemplo: se o seu nome for João Flores da Silva, pode mostrar “Bem-vindo à Loja do
João Flores da Silva” ou “Esta é a Loja Desconto da Cidade, bem-vindo! Aqui quem fala
é João Flores da Silva”.
2. Diga ao usuário que fará uma análise de crédito dele. Para tal, peça que digite o cargo na
empresa em que trabalha atualmente, o salário e o ano de nascimento.
3. Mostre ao usuário o cargo, o salário e o ano de nascimento que digitou.

      ATP – Etapa 2
Agora, vamos fazer uma análise de crédito do usuário para saber quanto ele poderá comprar na nossa
loja. Assim, continue do ponto em que parou na etapa 1 e, usando o mesmo código, adicione os
seguintes passos:
1. Mostre na tela a idade aproximada do usuário. Você pode fazer isso ao subtrair o ano em que
estamos pelo ano de nascimento que ele digitou.
2. Mostre quanto o cliente poderá gastar na sua loja (o limite de gasto), calculado da seguinte
forma: [salário x (idade / 1.000)] + 100.

      ATP – Etapa 3
Agora, vamos verificar se o produto que solicitamos ao usuário pode ser realmente comprado por
ele (ou não). Aqui, vamos usar o seu nome completo para montar a lógica.
Atenção! Vamos usar como lógica o seu nome completo e não o nome do usuário. A partir de agora,
quando falarmos “quantidade de caracteres do seu primeiro nome”, equivale à quantidade de letras
do seu primeiro nome. Por exemplo, se o seu nome completo é João Flores da Silva, isso seria igual 
a quatro. Quando falarmos “quantidade de caracteres do seu nome completo”, contaremos também
espaços e hifens. No mesmo exemplo, seria igual a 20.
1. Solicite ao cliente que digite o nome de um produto e o preço dele.
2. Se o valor do produto for menor ou igual a 60% do limite que o cliente tem para gastar, mostre
a mensagem “Liberado!”. Se estiver entre 60% e 90%, mostre a mensagem “Liberado ao
parcelar em até 2 vezes”. Se estiver entre 90% e 100%, mostre a mensagem “Liberado ao
parcelar em 3 ou mais vezes”. Caso contrário, mostre a mensagem “Bloqueado”.
3. Se o valor do produto estiver entre a quantidade de caracteres do seu nome completo e
a idade do cliente, mostre que ele terá um desconto igual à quantidade de caracteres do seu
primeiro nome.
4. Mostre também ao cliente o valor do produto com o desconto.
