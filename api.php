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
