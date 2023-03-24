CREATE TABLE IF NOT EXISTS `tipo_aplicaciones` (
  `identificador` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `nombre` varchar(200) COLLATE utf8_spanish_ci NOT NULL,
  `puerto` varchar(20) COLLATE utf8_spanish_ci NOT NULL,
  `estado` varchar(50) COLLATE utf8_spanish_ci NOT NULL,
  `tipo` varchar(50) COLLATE utf8_spanish_ci NOT NULL,
  `lenguaje` varchar(50) COLLATE utf8_spanish_ci NOT NULL,
  PRIMARY KEY (`identificador`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `tipo_aplicaciones`
--

INSERT INTO `tipo_aplicaciones` (`nombre`, `puerto`, `estado`, `tipo`, `lenguaje`) VALUES
('Monitoreo de temperatura', 'D2', 'Activo', 'Monitoreo', 'Python'),
('Control de riego automático', 'D5', 'Inactivo', 'Control', 'C++'),
('Detección de plagas', 'A1', 'Activo', 'Detección', 'Java'),
('Monitoreo de niveles de luz', 'A2', 'Inactivo', 'Monitoreo', 'Python'),
('Monitoreo de humedad', 'D3', 'Activo', 'Monitoreo', 'C#');
COMMIT;