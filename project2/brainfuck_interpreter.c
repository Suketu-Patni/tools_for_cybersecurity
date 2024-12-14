/*
I have implemented the interpreter exactly according to the rules, but the only programs that seem to 
produce the correct output are those in which the only task is to print an unchanging piece of text. 
So there's no actual programmatic stuff that seems to work. (idk why actually)
I have given some sample programs that work also at the end.
*/

#include <stdio.h>
#include <stdlib.h>

#define STREAM_SIZE 30000 // maximum length of the cell stream the program will operate on 

void execute_brainfuck(const char *code) {

    /*
    brainfuck rules (copied from wikipedia)

    Symbol 	Meaning
    < 	    Decrement the data pointer by one (to point to the next cell to the left).
    > 	    Increment the data pointer by one (to point to the next cell to the right).
    + 	    Increment the byte at the data pointer by one.
    - 	    Decrement the byte at the data pointer by one.
    . 	    Output the byte at the data pointer.
    , 	    Accept one byte of input, storing its value in the byte at the data pointer.
    [ 	    If the byte at the data pointer is zero, then instead of moving the instruction
            pointer forward to the next command, jump it forward to the command after the 
            matching ] command.
    ] 	    If the byte at the data pointer is nonzero, then instead of moving the instruction 
            pointer forward to the next command, jump it back to the command after the matching
            [ command.[a]
    */

    char stream[STREAM_SIZE] = {0};

    char *data_pointer;
    data_pointer = &stream[STREAM_SIZE/2]; // initially data pointer points to middle of stream, so decrementing
    // pointer is possible

    const char *instruction_pointer = code; // the pointer to a character in the program
    // const char because only the pointer can be incremented, not the data it points to


    while (*instruction_pointer) {

        switch (*instruction_pointer) {

            case '>':
                data_pointer++;
                break;

            case '<':
                data_pointer--;
                break;

            case '+':
                (*data_pointer)++;
                break;

            case '-':
                (*data_pointer)--;
                break;

            case '.':
                printf("%c", *data_pointer);
                break;

            case ',':
                *data_pointer = getchar();
                break;

            case '[':
                // in between there might be many '[' and ']'
                if (!(*data_pointer)) {
                    for (int bracket_number = 1; bracket_number != 0; instruction_pointer++) {
                        if (*instruction_pointer == '[') {
                            bracket_number++;
                        } else if (*instruction_pointer == ']') {
                            bracket_number--;
                        }
                    }
                    // now instruction pointer will be pointing to just after the matching ']'
                }

                break;

            case ']':
                if (*data_pointer) {

                    instruction_pointer -= 2; // ignore the current ']'

                    for (int bracket_number = 1; bracket_number != 0; instruction_pointer--) {
                        if (*instruction_pointer == ']') {
                            bracket_number++;
                        } else if (*instruction_pointer == '[') {
                            bracket_number--;
                        }
                    }
                    // now instruction pointer will be pointing to exactly the matching '['
                    instruction_pointer++;     
                }

                break;

            default:
                // character is ignored
                break;
        }
        ++instruction_pointer;
    }
}

int main(int argc, char *argv[]) {

    if (argc < 2) {
        // not enough arguments given
        fprintf(stderr, "Usage: %s \"<brainfuck code>\"\n", argv[0]);
        return 1;
    }

    execute_brainfuck(argv[1]);

    return 0;
}

/*
Sample programs that work:
1) -[------->+<]>-.-[->+++++<]>++.+++++++..+++.[->+++++<]>+.------------.---[->+++<]>.-[--->+<]>---.+++.------.--------.-[--->+<]>.[--->+<]>-..
2) -[--->+<]>-.[---->+++++<]>-.+.++++++++++.+[---->+<]>+++.-[--->++<]>-.++++++++++.+[---->+<]>+++.[-->+++++++<]>.++.-------------.[--->+<]>---..+++++.-[---->+<]>++.+[->+++<]>.++++++++++++..---.[-->+<]>--------.>++++++++++.
3) -[----->+<]>--.-----.++++++.------.+++++++.-------.++++++++.--------.+++++++++.---------.++++++++++.----------.+++++++++++.-----------.++++++++++++.------------.+++++++++++++.-------------.+++++.-.----.+++++..-----.+++++.+.------.+++++.++.-------.+++++.+++.--------.+++++.++++.>++++++++++...
*/