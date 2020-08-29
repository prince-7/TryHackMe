#!/usr/bin/env python3

import angr
import claripy

base_addr = 0x00100000
success_address = 0x0010111d
failure_address = 0x00101100
flag_length=15

project = angr.Project("./a.out", main_opts = {"base_addr" : base_addr})
flag_chars = [ claripy.BVS(f"flag_char{i}",8) for i in range(flag_length) ]
flag = claripy.Concat( *flag_chars + [claripy.BVV(b"\n")] )

state = project.factory.full_init_state(
	args = ["./a.out"],
	add_options= angr.options.unicorn,
	stdin= flag,
)


for k in flag_chars:
	state.solver.add(k>=ord('!'))
	state.solver.add(k<=ord('~'))
sim_manager = project.factory.simulation_manager(state)
sim_manager.explore(find=success_address,avoid=failure_address)

if (len(sim_manager.found)> 0 ) :
	for found in sim_manager.found:
		print(found.posix.dumps(0))