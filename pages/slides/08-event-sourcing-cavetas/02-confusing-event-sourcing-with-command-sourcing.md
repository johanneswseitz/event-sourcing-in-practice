## Command Sourcing

<div class="container_12">
	<div class="grid_6">
		<h3>Event Sourcing</h3>
		<ul>
			<li>Persist only changes in state</li>
		</ul>
		<img src="static/img/deposit-performed-event-v1.png"/>
		<ul>
			<li>Bit harder to implement</li>
			<li>Replay may be side-effect free</li>
		</ul>
	</div>
	<div class="grid_6">
		<h3>Command Sourcing</h3>
		<ul>
			<li>Persist Commands</li>
		</ul>
		<img src="static/img/perform-deposit-command.png"/>
		<ul>
			<li>Easier to implement</li>
			<li>Would replay side-effects</li>
		</ul>
	</div>
</div>