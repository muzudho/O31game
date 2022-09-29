# Author: hissatupassenger
# Arrangement: Muzudho (julia分からん)

# mexする。
#
# num_list は局面の集合か
#
# Author: hissatupassenger
# Arrangement: Muzudho (julia分からん)
function mex(num_list)
    # 空っぽ
    if num_list ==[]
        return 0
    end

    if num_list ==[0]
        return 1
    end
   N = length(num_list)
   ord_num_list = sort(num_list)
   if ord_num_list[1] !=0
       return 0
   end
   i = 1
   while i != N
       if ord_num_list[i] + 1 == ord_num_list[i+1]
	   i = i+1
	   continue
       else
	   return i
       end
   end
   return N
end

# グランディ数を求める
#
# - mex を使う
function grundy(grun_seq,subt)
	N = length(grun_seq)
	return mex([grun_seq[N+1-i] for i in subt if i<N+1])
end

function z_function(strn)
	N = length(strn)
	z_result = zeros(Int,N)
	left_pointer, right_pointer = 1, 1
	for i in 2:N
        	if i<=right_pointer
                	min_edge = min(right_pointer - i, z_result[i - left_pointer])
                	z_result[i] = min_edge
        	end

		while go_next(i, z_result, strn)
			z_result[i] = z_result[i] + 1
		end
		if i + z_result[i] - 1 > right_pointer
			left_pointer, right_pointer = i, i + z_result[i]
		end
	end
	return z_result
end

go_next(i, z_result, s) = i - 1 + z_result[i] < length(s) && s[z_result[i] + 1] == s[i - 1 + z_result[i] + 1]

function main()
	cur =[];
	subt = [1,4,10]
	perio = []
	for i in 0:10000
		print(grundy(cur,subt))
		print(" ")
		cur = append!(cur,grundy(cur,subt))

	end
	print(cur)
end

main()