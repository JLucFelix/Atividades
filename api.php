<?php

use Illuminate\Http\Request;
use Illuminate\Support\Facades\Route;

Route::get ('/teste', function(): string {
    return "hello world";
});

Route::get('/user', function (Request $request) {
    return $request->user();
})->middleware('auth:sanctum');

Route::get ('/contagem_jean', function(){
    for($i= 1; $i<100; $i++){
        dd($i);
        if($i%2==0){
            echo $i,"\n";
        }
    }
});

Route::get ('/contagem_primos', function(){
    for ($i=2; $i<=100; $i++){
        $primo = true;
        for($j = 2; $j<$i; $j++){
            if($i%$j == 0 ){
                $primo = false;
                break;
            }
        }
        if($primo){
            echo $i . "\n";
        }
    }
});

Route::get('/users/{id}', function($id){
    return $id;
});

Route::get('contagem_rota/{contagem}', function($contagem){
    for ($i =0; $i<$contagem + 1; $i++){
        echo $i . "\n";
    }
});

Route::get('par_impar/{numero}', function($numero){
    if($numero%2==0){
        return 'Par';
    }
    else{
        return 'Impar';
    }
});

Route::get('primo/{numeroprimo}', function($numeroprimo){
    $resultado = 0;
    for ($i=2; $i<$numeroprimo; $i++){
        if ($numeroprimo % $i == 0){
            $resultado++;
            break;
        } 
    }
    if ($resultado == 0){
        echo 'É primo';
    }
    else {
        echo 'Não é primo';
    }
});

Route::get('contagem/{numero1}/{numero2}', function($numero1, $numero2){
    for ($i =$numero1; $i<$numero2; $i++){
        echo $i . "\n";
    }
});

Route::get('calculadora/{numero1}/{numero2}',function($numero1,$numero2){
    $resultado = $numero1 + $numero2;
    echo 'O resultado é ', $resultado;  
});

Route::get('teste_query', function(Request $request){
    $valor1 = $request->query("valor1");
    $valor2 = $request->query("valor2", "valor_padrão");
    echo $valor1;
    echo "\n";
    echo $valor2;
});

Route::get('valor_divisivel', function(Request $request){
    $valor1 = $request->query("valor1");
    $valor2 = $request->query("valor2", "Deu zica");
    if ($valor1%$valor2==0){
        echo $valor1, ' é divisível por ', $valor2;
    }
});

Route::get('calculadora/{tipo_calculo}', function(Request $request, $tipo_calculo){
    $valor1 = $request->query("valor1");
    $valor2 = $request->query("valor2", "Deu zica");
    if ($tipo_calculo == 1){
        $soma = $valor1 + $valor2;
        echo 'resultado da soma é ', $soma; 
    }
    if ($tipo_calculo == 2){
        $subtracao = $valor1 - $valor2;
        echo 'resultado da subtração é ', $subtracao;
    }
    if ($tipo_calculo == 3){
        $divisao = $valor1/$valor2;
        echo 'resultado da divisão é ', $divisao;
    }
});

Route::get('mensagem', function(){
    echo 'Olá Mundo';
});

Route::post('mensagem', function(){
    echo 'Olá Pessoas';
});
//CALD ou CULD, Criar, Atualizar, Listar, Deletar.

Route::post('dados', function(Request $request){
    $nome = $request->input('nome');
    $email = $request->input('email', 'emailpadrao@teste.com');
    return response()->json(
        [
            "nome"=>$nome,
            "email"=>$email
        ]
    );
});
