# SSTF (Shortest Seek Time First) - Kernel Linux 4.13.9

- José Eduardo Rodrigues Serpa (20200311) 

- Nicolle Canceri Lumertz (20103640)

## ***Preparando a emulação***
Para utilizar o escalonador SSTF no buildroot será necessário primeiro criar a imagem do disco. Para isso, no diretório ./buildroot execute:

```
$ dd if=/dev/zero of=sdb.bin bs=512 count=2097152
```

Também será necessário compilar o módulo sstf-iosched no diretório ./modules. Para isso, existe um arquivo C no diretório do buildroot chamado 'compile.c' que compila tanto o módulo necessário como também o próprio buildroot e executa a emulação com os parâmetros necessários para a correta execução.

Portanto, compile o arquivo C utilzando o compilador da máquina local como por exemplo:

```
$ gcc -o compile compile.c
```

Em seguida execute o arquivo ./compile para entrar na emulação.

## ***Dentro do qemu***

Para utiliar o escalonador com política de SSTF, dentro do qemu execute:

```
$ modprobe sstf_iosched
$ echo sstf > /sys/block/sdb/queue/scheduler
$ cat /sys/block/sdb/queue/scheduler
noop deadline cfq [sstf]
```

O resultado do ultimo comando deve mostrar o escalonador sstf selecionado entre colchetes.

Por fim, para gerar estresse no disco, fazendo multiplas requisições simulando um ambiente multiprogramado, execute o seguinte comando:

```
sector_read
```

Será exibido na tela todas as rquisições adicionadas e despachadas pelo escalonador de disco.
