format long
count = 344;
while true 
    cube = count ^ 3;
    count = count +1;
    permutations = perms(int2str(cube));
    count_perm = 0;
    permutations = transpose(permutations);
    for i=permutations
        num = 0;
        power = 0;
        num = num +  str2double(i)*10^power;
        power = power + 1;
        display(count_perm);
        display(count);
        if mod(nthroot(num,3),1) == 0 && numel(num2str(num)) == numel(num2str(count^3)) 
            count_perm = count_perm + 1;
        end
        if power == 8
            power = 0;
            num = 0;
        end
    end
    if count_perm == 4
        DISP(count);
        exit
    end
end