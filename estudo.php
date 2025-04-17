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
    ?>


</body>

</html>