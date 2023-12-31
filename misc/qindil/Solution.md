# 9indil
## Write up

we were given this 

```c
#include <stdio.h>
#include <string.h>
#include <signal.h>
#include <fcntl.h>
#include <unistd.h>

int should_exit = 0;
void handle_interrupt(int sig)
{
    should_exit = 1;
}

void process_input(const char *input)
{
    char full_path[512];
    snprintf(full_path, sizeof(full_path), "../9indil/../Tooo0Cl0se/../1minute_takedown/../Tooo0Cl0se/No1isHere/../../Tooo0Cl0se/0ne_Sh0t/../../1minute_takedown/%s", input);

    int file = open(full_path, O_RDONLY);
    int seekclick;
    size_t len = strlen(input);
    seekclick = full_path[131] - '0';
    // lseek(file, seekclick, SEEK_SET);
    if (file != -1)
    {
        if (seekclick == 1)
        {
            seekclick = 0;
        }
        lseek(file, seekclick, SEEK_SET);

        char flag[256];
        int bytesRead = read(file, flag, sizeof(flag) - 1);
        if (bytesRead != -1)
        {
            flag[bytesRead] = '\0';
            printf("Go print your flag %s:", flag);
        }
        else
        {
            printf("Try Again.\n");
        }

        close(file);
    }
    else
    {
        printf("Try Again .\n");
    }
}

int main()
{
    signal(SIGINT, handle_interrupt);
    while (!should_exit)
    {
        printf("Navigate wisely: ");
        fflush(stdout);

        char input[256];
        if (fgets(input, sizeof(input), stdin) == NULL)
        {
            break;
        }

        size_t len = strlen(input);
        if (len > 0 && input[len - 1] == '\n')
        {
            input[len - 10] = '\0';
        }

        process_input(input);
    }

    return 0;
}

```

we specify the path of the file that we want to open and we obviosly want to open the flag file

the relative path is 
```
"../9indil/../Tooo0Cl0se/../1minute_takedown/../Tooo0Cl0se/No1isHere/../../Tooo0Cl0se/0ne_Sh0t/../../1minute_takedown/
```

so we need to go back to the precedent directory and open the flag file in the **9indil** directory 

that will be something like this 
```
../9indil/flag
```

but there is an interesting part of the code remove the last 9 charecters from our input
```c
        size_t len = strlen(input);
        if (len > 0 && input[len - 1] == '\n')
        {
            input[len - 10] = '\0';
        }
```

so we can easily trick this by adding 9 random charecters to our input

```
../9indil/flag123456789
```

and we get the flag

>flag : shellmates{G0ooD_J0b_y0u_did_it_Aga1n}


<img src="./pow.png"
     alt="Markdown Monster icon"
     style="
     width: 80%;
     diplay: box;"
/>