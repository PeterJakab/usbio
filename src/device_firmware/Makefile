MCU:=18f14k50
MCC:=/opt/microchip/mplabc18/v3.36/
MCCFLAGS=-Ou- -Ot+ -Ob+ -Op+ -Or+ -Od- -Opa+ -Om+ -On+ -Os+

default: usbio.hex

%.o: %.c
	$(MCC)/bin/mcc18 -p=$(MCU) /i"$(MCC)/h" "$^" -fo="$@" $(MCCFLAGS)
usbio.hex: usbio.o
	$(MCC)/bin/mplink -p$(MCU) -l"$(MCC)/lib" $^ -u_CRUNTIME -z__MPLAB_BUILD=1 "$(MCU)_g.lkr" -m"usbio.map" -w -o"usbio.cof" -i
	$(MCC)/bin/mp2cod usbio.cof
clean:
	rm -f *.o *.hex *.lst *.map *.err *.cof *.cod
