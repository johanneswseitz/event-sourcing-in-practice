## Problem: Events vs Command

* Confusing Event Sourcing and Command Sourcing

<div class="container_12">
	<div class="grid_6">
		<h4>Event Sourcing</h4>
		<ul>
			<li>Persist only changes in state</li>
			<li>Replay can be side-effect free</li>
		</ul>
		<img src="static/img/deposit-performed-event-v1.png"/>
	</div>
	<div class="grid_6">
		<h4>Command Sourcing</h4>
		<ul>
			<li>Persist Commands</li>
			<li>Replay may trigger side-effects</li>
		</ul>
		<img src="static/img/perform-deposit-command.png"/>
	</div>
</div>