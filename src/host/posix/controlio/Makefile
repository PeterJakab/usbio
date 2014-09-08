controlio: controlio.o
	$(CC) $(LDFLAGS) -o $@ $^ -l usb
%.o: %.c
	$(CC) $(CFLAGS) -c $<
clean:
	rm *.o controlio

