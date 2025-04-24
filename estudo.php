<!DOCTYPE html>
<html>

<body>

    <h1>Estudo</h1>


    <?php
    //comentando em uma linha só
    $txt = /* comentando no meio */ "Pamonha";
    echo "<p>Eu amo $txt!</p>";
    echo "<p>Eu amo" . "\n" . $txt . "!</p>";

    $a = 4;
    $b = 2;
    echo $a + $b . "<br>";
    var_dump($a);
    echo "<p>variável global: $a</p>";
    function testandofuncao()
    {
        echo "<p>Variável global impossível dentro de função</p>";
        $x = 10;
        echo "<p>Variavél local possível dentro da função: $x</p>";
    }
    testandofuncao();
    echo "<p>Variável global: $a</p>";
    echo "<p>Variável local fora dá erro</p>";

    function variavelglobal()
    {
        global $a, $b;
        $resultado = $a + $b;
        echo "resultado da variáveis globais $a e $b = $resultado";
        //ARRAY GLOBALS (Todas as variáveis globais)
        $GLOBALS['a'] = $GLOBALS['b'] + $GLOBALS['a'];
    }
    variavelglobal();
    echo "<P>Usando a variáel $ GLOBALS $a</p>";

    //Palavra-chave estática
    function statickeyword()
    {
        static $y = 0;
        echo $y;
        $y++;
    }
    statickeyword();
    statickeyword();
    statickeyword();

    //o echo pode ser udados das seguintes maneiras
    echo "<p>Olá</p>";
    echo ("<p>Olá</p>");
    //Formas de mostrar o texto
    echo "<h2>PHP é foda</h2>";
    echo "Olá mundo<br>";
    echo "Estou aprendendo PHP!<br>";
    echo "Esta ", "String ", "Foi ", "Feita ", "Com multiplos parametros";
    //print pode ser com ("") ou apenas ""
    print "<p>Olá com PRINT";
    $txt1 = "Olá com variável";
    print "<p>$txt1</p>";

    //matematica no php
    echo (pi()), "</p>";
    echo (min(0, 2, 33, 5, 60, 10, 22)), " Minimo</p>";
    echo (max(0, 2, 33, 5, 60, 10, 22)), " Maximo", "</p>";
    echo (abs(-6.7)), "</p>";

    echo (sqrt(64)), "</p>";
    echo (rand()), "</p>";
    echo (rand(10, 100)), "</p>";

    define("Saudacao", "Olá tudo bem");
    echo Saudacao, "</p>";
    const meucarro = "uno";
    echo meucarro, "</p>";

    define("carros", [
        "bmw",
        "jaguar",
        "Toyota"
    ]);
    print_r(carros, "</p>");
    /*
    Constantes magicas
    __CLASS__ retorna o nome da classe.
    __DIR__ retorna o diretorio do arquivo
    __FILE__ o nome do arquivo incluindo o caminho
    __FUNCTION__ o nome da função retorna
    __LINE__ O atual numero da linha
    __METHOD__ usado na função que pertence a uma classe, retorna nome
    da função e classe.
    __NAMESPACE__ o nome do namespace é retornado
    __TRAIT__ se usado dentro de um trait o nome do trait é retornado
    ClassName::class retorna o nome da classe especificada e o nome do 
    namespace se houver.
    */







    ?>


</body>

</html>
