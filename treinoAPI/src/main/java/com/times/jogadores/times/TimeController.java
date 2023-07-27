package com.times.jogadores.times;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import jakarta.transaction.Transactional;

@RestController
@RequestMapping("/times")
public class TimeController {

	@Autowired
	private TimeRepository repository;
	
	@GetMapping
	public List<Time> listar() {
		return repository.findAll();
	}
	
	@PostMapping
	@Transactional
	public void criar(@RequestBody DadosCadastroTime dados) {
		repository.save(new Time(dados));
	}
	
}
