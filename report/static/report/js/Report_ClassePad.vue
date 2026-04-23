<script>
export default{
	props:['label']
}
</script>

<template>
	<div style="
			border-style:solid;
			font-weight: bold;
			background-image: linear-gradient(135deg,#579fd1,#eaf3fc);
			padding: 5px;
			margin: 5px;
			display: inline-block;
			border-width: 2px;
			border-radius: 5px;
			border-color: #579fd1;
			width: 40px;
			text-align: center;
		"
	>
		{{	label }}
	</div>
</template>