controlio: controlio.o
	$(CC) $(LDFLAGS) -o $@ $^ -lusb
%.o: %.c
	$(CC) $(CFLAGS) -c $<
clean:
	rm *.o controlio
