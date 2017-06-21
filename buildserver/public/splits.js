function wsplit_get_param(key, lines, index, dispatch, is_opt)
{
	if(lines[index].startsWith(key + '='))
	{
		dispatch(lines[index].substring(key.length + 1))
		return index + 1;
	}

	if(is_opt)
	{
		return index;
	}

	throw "Invalid WSplit - Missing key: " + key
}

function populate_split_row(r, arr)
{
	for(let i = 0; i < arr.length; ++i)
	{
		let c = r.insertCell(-1)
		c.innerHTML = arr[i]
	}
}

function set_download(str)
{
	document.getElementById('download').innerHTML = str
}

function get_rule(index)
{
	return document.getElementById('rule_' + index).value
}

function collects_life(index)
{
	return document.getElementById('collect_' + index).checked
}

function rebuild_download()
{
	var pups_collected = 0
	var splits = document.getElementById('split_table').rows.length - 1

	console.log(splits)
	var worlds;

	if(8 == splits)
	{
		worlds =
		[
			[  0,  1, -1, -1 ],
			[ -1, -1, -1, -1 ],
			[ -1, -1, -1, -1 ],
			[  2,  3, -1, -1 ],
			[ -1, -1, -1, -1 ],
			[ -1, -1, -1, -1 ],
			[ -1, -1, -1, -1 ],
			[  4,  5,  6,  7 ]
		]
	}
	else if(32 == splits)
	{
		var total = 0
		worlds = []

		for(var w = 0; w < 8; ++w)
		{
			v = []
			for(var i = 0; i < 4; ++i)
			{
				v.push(total++)
			}
			worlds.push(v)
		}
	}
	else
	{
		set_download('I dont understand anything. I broke really bad <.<')
		return
	}

	var num_pups = 0
	var prev = 0

	for(var i = 0; i < worlds.length; ++i)
	{
		for(var x = 0; x < worlds[i].length; ++x)
		{
			var rule_index = worlds[i][x]

			if(-1 != rule_index)
			{
				let rule = Number(get_rule(rule_index))

				if(rule > 9999)
				{
					set_download('Max rule is 9999')
					return
				}

				if(prev > rule)
				{
					set_download('Earlier split has higher framerule than the one after')
					return
				}

				prev = rule
				worlds[i][x] = rule + ':' + num_pups

				if(collects_life(rule_index))
				{
					if(++num_pups > 2)
					{
						set_download('You can collect 2 power-ups at most')
						return
					}
				}
			}
			else
			{
				worlds[i][x] = '0:0'
			}
		}
	}

	var dl = '/build?'

	for(var i = 0; i < worlds.length; ++i)
	{
		for(var x = 0; x < worlds[i].length; ++x)
		{
			dl += 'w' + (i + 1) + '=' + worlds[i][x] + '&'
		}
	}
	console.log(dl)

	set_download('<a href="' + dl +  '">Download Ready!</a>')
}

function update_splits()
{
	try
	{
		var index = 0;
		let lines = document.getElementById('wsplit').value.trim().split('\n')

		index = wsplit_get_param('Title', lines, index, function(v) {
			document.getElementById('title_id').innerHTML = v
		})
		index = wsplit_get_param('Goal', lines, index, function(v) {}, true)
		index = wsplit_get_param('Attempts', lines, index, function(v) {
			document.getElementById('attempts_id').innerHTML = v
		})
		index = wsplit_get_param('Offset', lines, index, function(v) {})
		index = wsplit_get_param('Size', lines, index, function(v) {})

		let splits = []
		let num_splits = lines.length - index - 1;

		if(8 != num_splits && 32 != num_splits)
		{
			throw 'Expected 8 or 32 splits, found: ' + num_splits
		}

		let tbl = document.createElement("TABLE");
		tbl.id = 'split_table'
		tbl.createTHead();
		tbl.createTBody();
		populate_split_row(tbl.tHead.insertRow(0), [ 'Name', 'Total', 'Duration', 'Rule', 'Collected Power-up?' ])

		var rule_offset = 0

		rules = []
		rules.push(Number(document.getElementById('start_rule').value))

		for(let i = 1; i < num_splits; ++i)
		{
			let v = lines[index++].split(',')
			if(4 != v.length)
			{
				throw 'Failed to parse split-entry, expected 4 tokens, got ' + v.length
			}

			v.splice(1, 1)
			let rule = (v[1] * 60) / 21

			if(8 != num_splits && (3 == i || 5 == i))
			{
				//
				// In warpless, all splits are split at Intermediate screen.
				// In any%, world 4-1 and world 8-1 are split in accordance with the Practice ROM.
				//
				rule_offset += 7
			}

			rule += Number(document.getElementById('start_rule').value)
			rule += rule_offset

			v.push('<input type="text" id="rule_' + i + '" value="' + Math.round(rule + rule_offset) + '" oninput="rebuild_download()" />')
			v.push('<input type="checkbox" id="collect_' + i + '" onclick="rebuild_download()" />')
			populate_split_row(tbl.insertRow(-1), v)
		}

		index++;

		document.getElementById('splits').innerHTML = ''
		document.getElementById('splits').appendChild(tbl)

		wsplit_get_param('Icons', lines, index, function(v) {})

		rebuild_download()
	}
	catch(err)
	{
		console.log(err)
		set_download(' ERROR - ' + err)
	}
}


