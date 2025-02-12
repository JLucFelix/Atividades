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
    for ($i=1; $i<=100; $i++){
        if($i / $i == 0){
            echo $i, "\n";
        }
    }
});