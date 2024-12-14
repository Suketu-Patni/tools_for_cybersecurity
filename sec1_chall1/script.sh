#!/bin/bash

file_to_7z=$(find . -maxdepth 1 -type f ! -name "*.*")

# echo $file_to_unzip
# echo $file_to_7z

generate_possible_pwds() {
    
    if [ $2 -eq 0 ]; then
        echo $(cat $1)
    elif [ $2 -eq 1 ]; then
        echo $(base16 $1)
    elif [ $2 -eq 2 ]; then
        echo $(base32 $1)
    else
        echo $(base64 $1)
    fi
}



# while true
# ---------------------------------------------------------------------------------
# Unzipping

num_times=0

while :
do
    # first check what type of file is there

    file_to_unzip=$(find . -name "*.zip")

    if [[ -z "$file_to_unzip" ]]; then # no unzip file found -> 7z rahega, unzip that it

        file_to_7z=$(find . -name "*.7z")
        pwd_file_for_7z=$(find . -maxdepth 1 -type f ! -name "*.*")

        for j in {0..3};
        do
            # sleep .1 
            7z x $file_to_7z -p`generate_possible_pwds $pwd_file_for_7z $j` -o`pwd`
            if [ $? = 0 ]; then
                break
            fi
        done

        # sleep .1

        rm $file_to_7z
        rm $pwd_file_for_7z

        ((num_times++))

        # sleep .1

        # break

        if [ -f ./flag ]; then
            break
        fi

    else # unzip rahega

        pwd_file_for_unzip=$(find . -maxdepth 1 -type f ! -name "*.*")

        for i in {0..3};
        do  
            # sleep .1
            unzip -P `generate_possible_pwds $pwd_file_for_unzip $i` $file_to_unzip -d .
            if [ $? = 0 ]; then
                break
            fi
        done

        # sleep .1
        
        rm $file_to_unzip
        rm $pwd_file_for_unzip
        
        # sleep .1

        ((num_times++))
    

        # flag_found=$(find . -name 'flag*')
        if [ -f ./flag ]; then
            break
        fi
    fi
    
done

echo $num_times
# ---------------------------------------------------------------------------------