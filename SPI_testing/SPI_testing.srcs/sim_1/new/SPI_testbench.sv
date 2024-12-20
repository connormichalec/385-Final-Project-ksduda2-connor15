`timescale 1ns/1ps

`define TEST_CYCLES_NUM 5000

`define SPI_WORD_LEN 8
`define TEST_BYTE 'b10011110

`define NUM_WORDS 'sd16

`define TEST_BYTE_LED_ON 'sd7
`define TEST_BYTE_LED_OFF 'sd15

`define SPI_CLK_DIV 'sd4

module testbench_spi;

	int test_cycles = 0;
	logic chip_clock;
	
	logic SIGNAL_CLOCK;
	logic SIGNAL_SS;
	logic SIGNAL_DATA;
	
	logic reset_spi;
	logic spi_ready;
	
	logic reset_spi2;
	logic spi_ready2;

	logic proc_word;
	logic proc_word2;
	logic process_next_word;
	logic process_next_word2;
	logic [`SPI_WORD_LEN - 1:0] data;
	
	logic [`SPI_WORD_LEN - 1:0] recv_tmp;
	logic [`SPI_WORD_LEN - 1:0] recv_data;
	
	logic test_signal_control;
	
	logic reset_div;
	logic divider_ready;
	logic divided_master_clock; 
	//Clock divider module
	clock_divider #( .DIV_N(`SPI_CLK_DIV) )	clkdiv ( .clk_in(chip_clock), .clk_out(divided_master_clock), .do_reset(reset_div), .is_ready(divider_ready) );

	spi_module 
	#( .SPI_MASTER (1'b1) )
	spi_master
	( .master_clock(chip_clock),
	.SCLK_OUT(SIGNAL_CLOCK),
  	.SCLK_IN(divided_master_clock),
  	.SS_OUT(SIGNAL_SS),
  	.SS_IN(),
	.OUTPUT_SIGNAL(SIGNAL_DATA),
	.processing_word(proc_word), 
	.process_next_word(process_next_word),
	.data_word_send(data),
	.INPUT_SIGNAL(),
	.data_word_recv(),
	.do_reset(reset_spi),
	.is_ready(spi_ready) );
	
	spi_module 
	#( .SPI_MASTER (1'b0) )
	spi_slave
	( .master_clock(chip_clock),
	.SCLK_OUT(),
  	.SCLK_IN(SIGNAL_CLOCK),
  	.SS_OUT(),
  	.SS_IN(SIGNAL_SS),
	.OUTPUT_SIGNAL(),
	.processing_word(proc_word2), 
	.process_next_word(process_next_word2),
	.data_word_send(),
	.INPUT_SIGNAL(SIGNAL_DATA),
	.data_word_recv(recv_tmp),
	.do_reset(reset_spi2),
	.is_ready(spi_ready2) );

	initial begin

		$dumpfile("test_data/output.vcd");
		$dumpvars();	
		
		test_cycles <= 0;	
		
		reset_div <= 1'b1;
		
		process_next_word <= 1'b0;
				
		process_next_word2 <= 1'b0;
		
		reset_spi <= 1'b1;
		
		reset_spi2 <= 1'b1;
		
		data <= 'sd0;
		
		chip_clock = 1'b0; //blocking

	end

	always begin
		
		if(divider_ready) begin
				reset_div <= 1'b0;
		
			if(spi_ready) begin
				reset_spi <= 1'b0;
			
					
				if(spi_ready2) begin
					reset_spi2 <= 1'b0;
		
					if(!proc_word) begin
			
						if(!process_next_word) begin
			
							if(data < 'sd15) data <= data + 'sd1;
							else data <= 'sd0;
		
						end
			
						process_next_word <= 1'b1;
			
					end
					else if (proc_word && process_next_word)  process_next_word <= 1'b0;
		
					if(!proc_word2) begin
			
						if(!process_next_word2) recv_data <= recv_tmp;
			
						process_next_word2 <= 1'b1;
			
					end
					else if (proc_word2 && process_next_word2)  process_next_word2 <= 1'b0;
			
					if(recv_data == `TEST_BYTE_LED_ON) test_signal_control <= 1'b1;
					else if(recv_data == `TEST_BYTE_LED_OFF) test_signal_control <= 1'b0;
		
				end
		
			end
		
		end
		
	chip_clock <= ~chip_clock;
	test_cycles <= test_cycles + 1;

	if (test_cycles >= `TEST_CYCLES_NUM - 1) $finish;		
		
        #31.25; //16 MHz

      	end
      	
endmodule