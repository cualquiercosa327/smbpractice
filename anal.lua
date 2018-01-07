--
-- Don't forget to update these two on code-changes
--
dump_advance_pc = 0x91A8
dump_load_pc = 0x8512
dump_hammer_pc = 0xC3EA

addr_random = 0x7a7
addr_frame = 0x09
addr_timer_ctrl = 0x077f
addr_enemy_timers = 0x796

function read_array(at, n)
	local s = ''
	for i = 0, (n - 1) do
		s = s .. string.format('%02X ', memory.readbyteunsigned(at + i))
	end
	return s
end

function get_pretty_frame()
	return string.format('Frame: %02X', memory.readbyteunsigned(addr_frame))
end

function do_dump_state()

	local data = {
		get_pretty_frame(),
		string.format('Timer CTRL: %02X', memory.readbyteunsigned(addr_timer_ctrl)),
		'Random: ' .. read_array(addr_random, 7),
		'Enemy Timers: ' .. read_array(addr_enemy_timers, 7)
	}

	for i, txt in ipairs(data) do
		gui.text(16, 16 + (i * 16), txt)
		emu.print(txt)
	end

	-- emu.pause()
end

function do_dump_hammer()
	string.format(get_pretty_frame())

-- memory.registerexecute(dump_advance_pc, do_dump_state);
-- memory.registerexecute(dump_load_pc, do_dump_state);
memory.registerexecute(dump_hammer_pc, do_dump_hammer);
