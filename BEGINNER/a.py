
def pshufb(x, mask):
    y = x.copy()
    for i in range(len(x)):
        y[mask[i]] = x[i]
    return y

SHUFFLE_MASK = [0x02, 0x06, 0x07, 0x01, 0x05, 0x0b, 0x09, 0x0e, 0x03, 0x0f, 0x04, 0x08, 0x0a, 0x0c, 0x0d, 0x00]
shuffled_input = ""
user_input = ""

print("Flag: ")
user_input = input()[:15]
shuffled_input = pshufb(user_input, SHUFFLE_MASK);

#  local_28 = SUB164(shuffled_input,0) + ADD32._0_4_ ^ XOR._0_4_;
#  uStack36 = SUB164(shuffled_input >> 0x20,0) + ADD32._4_4_ ^ XOR._4_4_;
#  uStack32 = SUB164(shuffled_input >> 0x40,0) + ADD32._8_4_ ^ XOR._8_4_;
#  uStack28 = SUB164(shuffled_input >> 0x60,0) + ADD32._12_4_ ^ XOR._12_4_;
#  res_cmp = strncmp(user_input,(char *)&local_28,0x10);
#  if ((res_cmp == 0) && (res_cmp = strncmp((char *)&local_28,EXPECTED_PREFIX,4), res_cmp == 0)) {
#    puts("SUCCESS");
#    return 0;
#  }
#  puts("FAILURE");
#  return 1;
#}