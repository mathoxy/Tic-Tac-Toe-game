#include <stdio.h>
#include <conio.h>
#include <stdbool.h>


// Array of characters
char arr[10] = {' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '};

void show_board();
int check_for_win();

int main()
{
    // Insert players' names
    char player1[12], player2[12];
    printf("*******MORPION GAME*******\n");
    printf("Player 1 Name : ");scanf("%s", &player1);
    printf("Player 2 Name : ");scanf("%s", &player2);

    printf("       %s: X ; %s: 0\n", player1, player2);
    int player = 1, choice, i = -1;
    char mark;

    while(i == -1){
        show_board();
        player = (player%2 == 0)?2 : 1;
        if(player == 1)
            printf("%s turn ", player1);
        else
            printf("%s turn ", player2);
        scanf("%d", &choice);
        mark = (player == 1)?'X' : '0';

        // Conditions
        if(choice == 14 && arr[1] == ' '){
            arr[1] = mark;
        }
        else if(choice == 15 && arr[2] == ' '){
            arr[2] = mark;
        }
        else if(choice == 16 && arr[3] == ' '){
            arr[3] = mark;
        }
        else if(choice == 24 && arr[4] == ' '){
            arr[4] = mark;
        }
        else if(choice == 25 && arr[5] == ' '){
            arr[5] = mark;
        }
        else if(choice == 26 && arr[6] == ' '){
            arr[6] = mark;
        }
        else if(choice == 34 && arr[7] == ' '){
            arr[7] = mark;
        }
        else if(choice == 35 && arr[8] == ' '){
            arr[8] = mark;
        }
        else if(choice == 36 && arr[9] == ' '){
            arr[9] = mark;
        }
        else{
            printf("Invalid value\n");
            player --;
            getch();
        }

        player ++;
        i = check_for_win();

    }
    show_board();
    player--;
    player = (player%2 == 0)?2 : 1;

    if(i == 1){
        switch(player){
            case 1: printf("%s Won", player1);
                    break;
            case 2: printf("%s Won", player2);
                    break;
        }
    }

    else if(i ==0)
        printf("GAME OVER\n");
    getch();


    return 0;
}
int check_for_win(){
    // Win cases

    // For rows
    if(arr[1] == arr[4] && arr[4] == arr[7] && arr[7] != ' ')
        return 1;
    if(arr[2] == arr[5] && arr[5] == arr[8] && arr[8] != ' ')
        return 1;
    if(arr[3] == arr[6] && arr[6] == arr[9] && arr[9] != ' ')
        return 1;

    // For lines
    if(arr[1] == arr[2] && arr[2] == arr[3] && arr[3] != ' ')
        return 1;
    if(arr[4] == arr[5] && arr[5] == arr[6] && arr[6] != ' ')
        return 1;
    if(arr[7] == arr[8] && arr[8] == arr[9] && arr[9] != ' ')
        return 1;

    // For diagonals
    if(arr[1] == arr[5] && arr[5] == arr[9] && arr[9] != ' ')
        return 1;
    if(arr[3] == arr[5] && arr[5] == arr[7] && arr[7] != ' ')
        return 1;

    // Game Over
    // else if(arr[1]!=' ' && arr[2]!=' ' && arr[3]!=' ' && arr[4]!=' ' && arr[5]!=' ' && arr[6]!=' ' && arr[7]!=' ' && arr[8]!=' ' && arr[9]!=' ')
    // Game Over
    bool over = false;
    for(int j=1; j<=9; j++){
        if(arr[j] != ' ' )
            over = true;
        else{
            over = false;
            break;
        }

    }
    if(over == true)
        return 0;

    // Continue
    else
        return -1;


}

void show_board(){
    printf("     4       5       6   \n");
    printf("         |      |       \n");
    printf("1    %c   |   %c  |   %c\n", arr[1], arr[2], arr[3]);
    printf("         |      |       \n");
    printf("  -------|------|------- \n");
    printf("         |      |       \n");
    printf("2    %c   |   %c  |   %c\n", arr[4], arr[5], arr[6]);
    printf("         |      |       \n");
    printf("  -------|------|------- \n");
    printf("         |      |       \n");
    printf("3    %c   |   %c  |   %c\n", arr[7], arr[8], arr[9]);
    printf("         |      |       \n");





}

