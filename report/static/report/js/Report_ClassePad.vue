<script>
	export default{
	props:['label','id']
}
</script>

<template>
	<a :href="'api/classe/'+id" style="color: black;">

	<div style="
			border-style:solid;
			font-weight: bold;
			font-size: 120%;
			background-image: linear-gradient(135deg,#579fd1,#eaf3fc);
			padding: 10px;
			margin: 5px;
			display: inline-block;
			border-width: 2px;
			border-radius: 5px;
			border-color: #579fd1;
			width: 50px;
			height: 50px;
			text-align: center;
		"
	>
		{{ label }}
	</div>
</a>

</template>